import threading
from pwn import *

def connect1(output, index):
    r = remote("nopsctf-broken-otp.chals.io", 443, ssl=True, sni="nopsctf-broken-otp.chals.io")
    r.sendlineafter(b"Enter your choice: ", b"1")
    r.sendlineafter(b"Please enter the message you wish to encrypt: ", b"\x00"*19)
    output[index] = r.recv().strip().split(b": ")[1].decode()

def connect2(output, index):
    r = remote("nopsctf-broken-otp.chals.io", 443, ssl=True, sni="nopsctf-broken-otp.chals.io")
    r.sendlineafter(b"Enter your choice: ", b"2")
    output[index] = r.recv().strip().split(b": ")[1].decode()

output = [None, None]

thread1 = threading.Thread(target=connect1, args=(output, 0))
thread2 = threading.Thread(target=connect2, args=(output, 1))

thread1.start()
thread2.start()

thread1.join()
thread2.join()

key = output[0]
enc_flag = output[1]

# works like 1/5 times cause snicat <<< nc
flag = xor(bytes.fromhex(key), bytes.fromhex(enc_flag))
print("Flag:",flag)
