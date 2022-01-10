#!/usr/bin/python3

import pwn

pwn.log.context_level = 'debug'
p = pwn.remote("host1.dreamhack.games", 9499)

p.interactive()
