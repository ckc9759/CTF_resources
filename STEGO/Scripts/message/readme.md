```py
from pwn import *

f1 = open('file1').read()
f2 = open('file2').read()

print len(f1), len(f2)

for i in range(len(f1)) :
   print f1[i], f2[i]
   
ord(f1[i]) --> ascii value

message = []
for i in range (len(f1)):
   if(f1[i]==f2[i]):
       message.append(f1[i])
print ''.join(message)
```

Only for reference not a real python code
