from pwn import *

'''
If I tell you there's a GORGE, you send back STOP
If I tell you there's a PHREAK, you send back DROP
If I tell you there's a FIRE, you send back ROLL
'''

map1={'GORGE':'STOP','PHREAK':'DROP','FIRE':'ROLL'}

r=remote('94.237.60.39',54920)


r.recvuntil(b"(y/n) ")
r.sendline(b"y")


r.recvuntil(b"!\n")

while True:
   inp=r.recvuntil(b"\n")
   inp=str(inp)
   inp2=inp[2:-3].replace(" ",'').split(',')
   print(inp2)
   payload=''
   for ii in inp2:
      payload+=map1[ii]+'-'
   payload=payload[:-1]
   print(payload)
   try:
      r.recvuntil(b"? ")
      r.sendline(payload)
   except e:
      r.interactive()
