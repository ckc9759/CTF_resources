# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 12:03:52 2023

@author: CHKRISH
"""

import random
import time
import datetime
import base64
from Crypto.Cipher import AES


flag = b"find_me"
iv = b"\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0"

c = "lQbbaZbwTCzzy73Q+0sRVViU27WrwvGoOzPv66lpqOWQLSXF9M8n24PE5y4K2T6Y"
c1 = base64.b64decode(c.encode('utf-8'))
c2 = base64.b64decode(c)

l1 = []
l2 = []

for i in range(0, 16-(len(flag) % 16)):
    flag += b"\0"

#ts_i = 1690934400
#ts_i = 1690934820
#ts_i = 1690934400
#ts_i = 1690993523975
#ts_i = 1691011711337
#ts_i = 1691011711338
ts_i = 1690986420000
inc = 1

i1 = 1

while ts_i <= 1690986479000:
    #seed = round(ts_i*1000)
    seed = ts_i
    random.seed(seed)

    key = []
    for i in range(0, 16):
        key.append(random.randint(0, 255))

    key = bytearray(key)

    cipher = AES.new(key, AES.MODE_CBC, iv)
    cipher2 = AES.new(key, AES.MODE_CBC, iv)

    p1 = cipher.decrypt(c1)
    p2 = cipher2.decrypt(c2)

    l1.append(p1)
    l2.append(p2)

    print(f'{i1} : {ts_i}')

    if b'flag' in p1 or b'flag' in p2:
        print(p1)
        print(p2)
        print('^'*100)
        break
    ts_i = ts_i+inc
    i1 = i1+1

'''
print(l1)
print()
print()
print(l2)
'''
