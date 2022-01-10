#!/usr/bin/python3

_data_offset = 0x2400
dec_string = ""

with open("./chall8.exe", "rb") as f:
    data = f.read()
    enc_string = data[_data_offset:_data_offset+20]

for i in range(0, len(enc_string)):
    for j in range(32, 127):
        tmp = int((j * 0xfb)) & 0xff
        if enc_string[i] == tmp:
            dec_string += chr(j)

print("Flag is DH{{{}}}".format(dec_string))
