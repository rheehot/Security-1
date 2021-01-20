#!/usr/bin/python

from hashlib import sha1
import threading

ref = str(input("Enter Your Reference: "))
salt = "salt_for_you"
index = int(input("Enter Index Number: "))
s_num = 10000000
e_num = 99999999+1
rge = int((e_num-s_num)/index)

def execute(index, ref, salt, start, rge):
    for a in range(start+rge*(index-1), start+rge*index):
        hs = str(a)+salt
        result = hs
        for i in range(500):
            result = sha1(result.encode('utf-8')).hexdigest()
        with open("/tmp/result{}.txt".format(index), 'a') as file:
            file.write("hash is : {}, key is : {}\n".format(result, hs))
        if str(result) == str(ref):
            print("key : {}".format(hs))

if __name__ == '__main__':
    for i in range(1, index+1):
        calc = threading.Thread(target=execute, args=(i, ref, salt, s_num, rge))
        calc.start()
