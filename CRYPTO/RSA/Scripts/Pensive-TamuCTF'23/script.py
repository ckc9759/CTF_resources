from pwn import *
context.log_level = "debug"

p = remote("tamuctf.com", 443, ssl=True, sni="numbers-pensive")
p.recvuntil(b"n = ")
n = int(p.recvline().strip())
p.recvuntil(b"\n")
e = 65537
p.recvuntil(b":")
p.sendline(b"-65537")
d = int(p.recvuntil(b"\n").strip())
p.recvuntil(b"If you can decrypt this, I'll give you a flag!\n")
c = int(p.recvline().strip())
m = pow(c, -d, n)
p.sendlineafter(b"Your answer: ", str(m).encode())
p.interactive()
# gigem{h4h4_numb3rs_ar3_s0_qu1rky}
