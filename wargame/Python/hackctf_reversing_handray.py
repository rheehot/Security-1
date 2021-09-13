#!/usr/bin/python3

import struct

_string_offset = 0x000010D8+0x8
_array_offset = 0x00001054+0xc
salt = [0]*33
dec_flag = ""

with open("/tmp/handray", "rb") as f:
    data = f.read()
    enc_flag = data[_string_offset:_string_offset+33].decode('utf-8')
    array = data[_array_offset:_array_offset+120]

def toTheNumeric(array):
    for i in range(int(len(array)/4)):
        salt[i] = struct.unpack("<I", array[i*4:i*4+4])[0]

def decoding(enc_flag, salt):
    enc = list(enc_flag)
    global dec_flag
    for i in range(len(enc_flag)):
        dec_flag += chr(ord(enc[i]) + salt[i])

toTheNumeric(array)
decoding(enc_flag, salt)
print(dec_flag)
