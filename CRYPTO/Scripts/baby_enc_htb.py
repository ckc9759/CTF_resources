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

#Bruteforce approach !
'''
encrypted_txt = "6e0a9372ec49a3f6930ed8723f9df6f6720ed8d89dc4937222ec7214d89d1e0e352ce0aa6ec82bf622227bb70e7fb7352249b7d893c493d8539dec8fb7935d490e7f9d22ec89b7a322ec8fd80e7f8921"
result = ""

ct = bytes.fromhex(encrypted_txt)
 
for char in ct:
    for val in range(33, 126):
        if ((123 * val + 18) % 256) == char:
            result += chr(val)
            break
 
print(result)
'''
