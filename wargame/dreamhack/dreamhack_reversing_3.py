#!/usr/bin/python

str_1 = "4960677463674266807869697B996D8868949F8D4DA59D45"
str_r = ""
last = []

for i in range(24):
    last.append(chr((int(str_1[i*2:i*2+2], 16)-i*2)^i))

str_r = "".join(last)
print(str_r)