#!/usr/bin/env python3

import itertools

with open("enc", "rb") as f:
    enc = f.readlines()[0]

char = "".join([chr(i) for i in range(32, 127)])
flag = ""

def logic(txt, length):
    global flag
    for i in range(length):
        for target in itertools.product(char, repeat = 2):
            tmp = ''.join(chr((ord(target[0]) << 8) + ord(target[1])))
            if tmp == list(txt.decode())[i]:
                flag += "".join(target)

logic(enc, len(enc.decode()))
#print(list(enc.decode())[1])
print(flag)
