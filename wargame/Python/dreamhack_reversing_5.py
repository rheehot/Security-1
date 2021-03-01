#!/usr/bin/python

import hextoList as htL

refBF = "ADD8CBCB9D97CBC492A1D2D7D2D6A8A5DCC7ADA3A1984C"
refAF = ['0x' + val for val in htL.hexStr(refBF)]

print(hex(refAF[22])-hex(refAF[21]))