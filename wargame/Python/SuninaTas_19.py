#!/usr/bin/python

val = str(input())

print(int(len(val)/8))

lst = []

for n in range(0,int(len(val)/8)):
    lst.append(val[int(8*n):int(8*n+8)])

dec = []
for a in range(0, len(lst)):
    dec.append(int(lst[a],2))

print(dec)

#cvt = []
#for a in range(0, len(dec)):
#    if(int(dec[a] == 32)):
#        cvt.append[chr(int(dec[a]))]
#    else:
#        if(int(dec[a])+17 > 90):
#            var = int(int(dec[a]+17-90))
#            print(type(dec[a]))
#            cvt.append[chr(int(int(dec[a])+var))]
#        else:
#            cvt.append[chr(int(dec[a])+int(17))]

cvt = "".join([chr(int(a)) for a in dec])

print(cvt)
#나중에 다시하자 지금은 너무 정신적으로 피폐해졌어...
#32가 공백 17개 쉬프트 아예 나중에 만드는 거 글자 수에 따라 자동 쉬프트로
