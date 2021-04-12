#!/usr/bin/python

from pwn import *

conn = pwn.remote("host1.dreamhack.games", 23419)
