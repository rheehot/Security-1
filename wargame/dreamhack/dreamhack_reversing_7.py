#!/usr/bin/python

_data_offset = 0x2400
decFlag = ""

def ROL(data, shift, size=8):
    shift %= size
    remains = data >> (size - shift)
    body = (data << shift) - (remains << size )
    return (body + remains)

with open("./chall7.exe", "rb") as pe:
    extract = pe.read()
    ansFlag = extract[_data_offset:_data_offset+0x1f]

for i in range(len(ansFlag)):
    for j in range(0x21, 0x7e+1):
        index = i & 0x7
        flag = ROL(j, i)
        flag = flag^i
        
        if ansFlag[i] == flag:
             decFlag += chr(j)

print(decFlag)

