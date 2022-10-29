From pwn import *

io = process('./pwnme')

io.sendlineafter(b'.',b'AAAAA')

io.interactive() or print(io.recvall().decode())
