#!/usr/bin/python

"""
This module made for reversing wargame.
"""

def hexStr(ref):
    strLen = int(len(ref)/2)
    conStr = []
    for i in range(strLen):
        conStr.append(ref[i*2:i*2+2])
    return conStr