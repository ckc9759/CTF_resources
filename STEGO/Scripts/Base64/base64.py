import base64

f = open("h.txt").read()
bytes = f.encode("ascii")

for i in range (0,30):
   ckc = base64.b64decode(bytes)
   bytes=ckc
   
print(ckc)

