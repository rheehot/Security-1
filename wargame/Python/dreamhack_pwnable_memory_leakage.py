#!/usr/bin/python3

import pwn

#pwn.context.log_level = 'debug'
p = pwn.remote("host1.dreamhack.games", 23487)

p.interactive()

"""
main+239 - print information 메뉴 선택 시 분기
main+281 - GIVE ME FLAG 메뉴 선택 시 분기
main+163 - Join 메뉴 선택 시 분기
main+330 - 위 case에 해당되지 않을 경우 분기

구조체를 사용할 경우 같은 시작 주소를 가지고 있는 것 같다. name과 age 모두 ebp-0x58 위치로 입력받는다.
name의 경우 0x10 Byte를 입력받으며 age의 경우 scanf로 입력받는다. 반면에 출력할 때는 name의 경우 ebp-0x58에서, age의 경우 0x48에서 가져온다.

어째서일까 fp로 아무것도 값을 못읽어온 이유는?
생각해보니 로컬에서 테스트할 경우 flag 파일이 없다는 점을 간과하고 있었다.


"""
