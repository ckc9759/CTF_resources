from Crypto.Util.number import long_to_bytes
from pwn import remote

io = remote("challs.actf.co", "32400")
n = int(io.readline().split()[-1].decode())
e = int(io.readline().split()[-1].decode())
c = int(io.readline().split()[-1].decode())
io.read()

# blinding attack
r = 2
x = (r**e*c) % n
io.sendline(str(x).encode())
y = int(io.readline().split()[-1].decode())

flag = y * pow(r,-1,n) % n
print(long_to_bytes(flag))
