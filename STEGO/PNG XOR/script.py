from itertools import *
from pwn import *
import string

header = b"\x89\x50\x4E\x47\x0D\x0A\x1A\x0A\x00\x00\x00\x0D\x49\x48\x44\x52"
charset = string.printable

key=""

with open('flag.png.xor','rb') as inf:
  file=inf.read()
  for i in range (len(header)):
    for c in charset:
      if header[i] == ord(xor(c.encode(),file[i])):
        key+=c
        print(key)
        break

        
        
# After we find the key

key = b'W3lc0me!'
with open('flag.png','wb') as outfile:
  outfile.write(xor(key,file))
  
  
