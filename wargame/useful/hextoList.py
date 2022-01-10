#!/usr/bin/python

"""
This module made for reversing wargame.
"""

def hexStr(ref, strLen):
    conStr = []
    for i in range(strLen):
        conStr.append('0x'+ref[i*2:i*2+2].lower())
            
    return conStr