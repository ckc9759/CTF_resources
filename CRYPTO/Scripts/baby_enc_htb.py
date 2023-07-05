'''
import string
from secret import MSG

def encryption(msg):
    ct = []
    for char in msg:
        ct.append((123 * char + 18) % 256)
    return bytes(ct)

ct = encryption(MSG)
f = open('./msg.enc','w')
f.write(ct.hex())
f.close()
'''

f=open('msg.enc','r')
a=f.read()
b=bytes.fromhex(a)
print(a)
print(b)
print(list(b))
c=list(b)

#int_val=int.from_bytes(b,"big")
#print(int_val)


pt=[]
for bb in c:
   bb-=18
   bb=179*bb % 256
   pt.append(bb)
   
print(bytes(pt))
   
# ct = ((123*char+18) % 256

#char=((ct-18)/123*256)%256
