### Pwntools

---

When writing exploits, first we import the pwn library.

```py
from pwn import *
```

Pwntools is a CTF framework and exploit developement library.

---

#### Accessing a remote server

```py
from pwn import *
r = remote('ckc_exploit.example.com',12345)

# Exploit goes here

r.send(asm(shellcraft.sh()))
r.interactive()
```

---

#### Receiving Data : 

```py
* recv(n) - Receive any number of available bytes.
* recvline() - Receive data until a newline is encountered.
* recvuntil(delim) - Receive data until a delimiter is found.
* clean() - Discard all buffered data
```

#### Sending Data : 

```py
* send(data) - Sends data
* sendline(line) - Sends data plus a newline
```

