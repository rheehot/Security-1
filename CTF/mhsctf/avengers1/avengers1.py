#!/usr/bin/env python3

import dis

def main():
    inp = input("What's the password")
    pwd = ''

    for i in range(len(inp)):
        pwd += chr(ord(inp[i]) + int(i % 7))

    comp = [102, 109, 99, 106, 127, 53, 116, 95, 122, 113, 120, 118, 100, 55, 51, 103, 57, 128]
    incor = False

    for i in range(len(pwd)):
        if pwd != chr(comp[i]):
            print("Incorrect Password")
            incor = True
            break

    if incor:
        pass
    else:
        print("Welcome!!")

def decode():
    pwd = ''
    comp = [102, 109, 99, 106, 127, 53, 116, 95, 122, 113, 120, 118, 100, 55, 51, 103, 57, 128]

    for i in range(len(comp)):
        pwd += chr(comp[i] - int(i % 7))
    return print(pwd)

if __name__ == '__main__':
    #dis.dis(main)
    decode()
