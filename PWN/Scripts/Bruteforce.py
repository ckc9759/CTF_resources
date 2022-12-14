# Each time u enter a part of flag, value increases 

So starting with HCTF{ we can bruteforce our flag
                      
from pwn import *

enc = 'HCTF{'
val = 0.14705882352941177
letter = 0

pause = True

while pause:
    io = remote('hctf.hackappatoi.com', 9001)
    cont = io.recvuntil('\n')
    io.sendline(enc + chr(letter))
    val2 = float(io.recvuntil('\n'))
    print(f'GOT: {val2}, index: {letter}')
    if val2 == 1.0:
        print(enc)
        pause = False
    elif val2 > val:
        enc += chr(letter)
        print(enc)
        val = val2
        letter = 33
    else:
        letter += 1
