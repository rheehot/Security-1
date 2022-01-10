#!/usr/bin/python3

from pwn import *

#p = process("./random")
p = remote("ctf.j0n9hyun.xyz", 3014)
v = process("./value")

key = int(v.recvline().decode('utf-8').strip("\n"))
p.sendlineafter(" : ", str(key))

log.info("key: " + str(key))
p.interactive()

