#!/usr/bin/python

hexStr = "242713c6c61316e647f5269647f54627132626c656f5c3c3f5e3e3"
ansStr = []
ans = []

"""
Hex value 저장을 위한 변수, 임시적으로 저장하기 위한 list, 최종 flag를 저장할 list 선언
"""

for i in range(int(len(hexStr)/2)):
    ansStr.append("0x"+hexStr[i*2:i*2+2])   # 합쳐져 있는 Hex value를 0x문자를 붙여 분리

for i in range(int(len(hexStr)/2)):
    for j in range(32, 126+1):
        tmp1= j >> 4
        tmp2 = (j << 4) & 0xf0
        tmp = hex(tmp1 | tmp2)
        print(tmp)
        if tmp == ansStr[i]:
            ans.append(chr(j))

"""
Logic을 분석해보면 다음처럼 동작한다.

1. 입력받은 문자열을 오른쪽으로 4만큼 비트 쉬프트한 뒤 eax에 저장한다.
2. 입력받은 문자열을 왼쪽으로 4만큼 비트 쉬프트한 뒤 0xF0와 AND 연산 후 ecx에 저장한다.
3. eax와 ecx를 OR 연산한 결과를 eax에 저장한다.
4. ecx에 정답 결과를 가져온 뒤 eax와 ecx가 일치하는지 확인한다.
"""

print("".join(ans))