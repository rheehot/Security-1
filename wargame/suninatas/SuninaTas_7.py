#/usr/bin/python

import requests as req, re

URL1 = "http://suninatas.com/challenge/web07/web07.asp"
URL2 = "http://suninatas.com/challenge/web07/web07_1.asp"

cookies = {"ASPSESSIONIDCSABRCRD":"PPMBMEKBHNLEEONKOKDEPHDI", "ASP.NET_SessionId":"micl012pqno1myet134mrn51"}
session = req.session()

while True:
    response1 = session.get(URL, cookies = cookies)
    response2 = session.get(URL2, cookies = cookies)
    
    if(response2.text.find("Your too slow") == -1):
        print(
