#!/usr/bin/python
import base64

msg = str(input())

lst = msg.split()

cvt = "".join([chr(int(a)) for a in lst])

print(cvt)

answer = base64.b64decode(cvt.encode('utf-8'))

print(answer.decode('utf-8'))
