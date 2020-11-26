import base64

user="admin"        
password="nimda"    #변환할 문자열 지정

buser = user.encode("UTF-8")
bpassword = password.encode("UTF-8")    #base64로 encoding 하기 위해선 byte 형태여야 한다.
                                        #아예 문자열을 선언할 때 b"admin" 이런 식으로 선언해도 된다.

for a in range(20):                     #20번 encoding 하기 위해서 반복문을 사용해준다. range() 안에 하나의
                                        #숫자만 써주면 0부터 주어진 숫자의 횟수만큼 반복한다.
    buser = base64.b64encode(buser)
    bpassword = base64.b64encode(bpassword) #base64로 encoding 해준다. base64 module을 import해야한다.

cryptuser = buser.decode("UTF-8")   
cryptpassword = bpassword.decode("UTF-8")   #byte 형식으로 encoding 되어 있던 것을 다시 decoding 해준다.


print(cryptuser)
print()
print(cryptpassword)
