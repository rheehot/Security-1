#!/usr/bin/python

import requests as req

cookies = {"ASP.NET_SessionId":"yknflzzx1htpmbhhuwcqjtai", "ASPSESSIONIDSADBSAQD":"LHAPHFIDIBDKMEFMGMJFJLPH"}
url = "http://suninatas.com/challenge/web22/web22.asp"
maxpass = 15
response = req.get(url, cookies=cookies)


