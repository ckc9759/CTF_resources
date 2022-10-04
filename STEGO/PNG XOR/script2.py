from itertools import *
from pwn import *
import string

charset = string.printable
header = b"Greatness is a transitory experience."

key = ""

with open('spi.ce','rb') as inf:
  file=inf.read()
  for i in range(len(header)):
     for c in charset:
        if header[i] == ord(xor(c.encode(),file[i])):
          key+=c
          print(key)
          break
          
key = b'DUN3'
with open('flag.txt','wb') as outfile:
   outfile.write(xor(key,file))
