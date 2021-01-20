#!/usr/bin/python

from hashlib import sha1

ref = "01d5ceeabd325c59be1189f83164ec0c56b5a25a"
salt = "salt_for_you"

for a in range(10000000, 99999999+1):
    hs = str(a)+salt
    result = hs
    for a in range(500):
        result = sha1(result.encode('utf-8')).hexdigest()
    if(result == ref):
        print("key is {} and salt is {}".format(hs, salt))
        break
