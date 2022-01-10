#!/usr/bin/python

import hextoList as htL

refBF = "ADD8CBCB9D97CBC492A1D2D7D2D6A8A5DCC7ADA3A1984C"
strLen = int(len(refBF)/2)

refAF = htL.hexStr(refBF, strLen)
refAF.reverse()

answer = [chr(0x4c)]

tmp = 0
for index in range(strLen - 1):
    if index == 0:
        sub = int(refAF[index+1], 0) - int(refAF[index], 0)
        tmp = sub
        answer.append(chr(sub))
        index += 1
        continue
    sub = int(refAF[index+1], 0) - tmp
    tmp = sub
    answer.append(chr(sub))
    index += 1

answer.reverse()
print("".join(answer))