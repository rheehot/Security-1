#!/usr/bin/python

a = 0xf0

b = a << 1

c = (b & 0x0ff) | 0x1

print(hex(b), hex(c))