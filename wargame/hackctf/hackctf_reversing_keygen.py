#!/usr/bin/python3

from pwn import *

p = remote("ctf.j0n9hyun.xyz", 9004)

enc_string = "OO]oUU2U<sU2UsUsK"
key = 72
result = ""
length = len(enc_string)

for i in range(0, length):
    for j in range(33, 126):
        tmp = ((j + 12) * key + 17) % 70 + 48
        if chr(tmp) == enc_string[i]:
            key = tmp
            result += chr(j)
            break

result = result[:-1]

log.info("Decoded String is {}".format(result))

p.sendlineafter(": ", result)
p.interactive()
