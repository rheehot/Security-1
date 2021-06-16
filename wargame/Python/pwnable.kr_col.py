#!/usr/bin/python3

def a2i(strVal):
    split = list(strVal)
    
    total = ord(split[0])*0x01000000+ord(split[1])*0x010000+ord(split[2])*0x0100+ord(split[3])*0x01
    return total

test = "ABCD"

