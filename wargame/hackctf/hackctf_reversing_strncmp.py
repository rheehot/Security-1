#!/usr/bin/python3

enc_flag = "OfdlDSA|3tXb32~X3tX@sX`4tXtz"
key = 7
dec_flag = [0] * len(enc_flag)

for i in range(len(enc_flag)):
    dec_flag[i] = chr(ord(enc_flag[i]) ^ key)

print("".join(dec_flag))
