import numpy as np
import re

def num(line):
    pattern = r'\d+'
    numbers = re.findall(pattern, line)
    numbers=[int(i) for i in numbers]
    return numbers
'''
Quick! These set of linear equations describe the secretes to time travel!
But the quantum state of the universe only gives us 10 mere seconds to solve them!!!

2974*a + 9870*b + 3119*c + 1052*d + 5712*e = 78279386
2161*a + 4536*b + 7646*c + 2461*d + 7108*e = 118386717
8849*a + 4940*b + 9429*c + 4263*d + 7545*e = 177729391
2646*a + 4141*b + 6931*c + 6026*d + 4054*e = 119264444
267*a + 548*b + 6676*c + 918*d + 1785*e = 71624331
a = ^Z
'''    
    
from pwn import *

r=remote('chals.swampctf.com',60001)

r.recvuntil(b"!!!")
r.recvuntil(b"\n\n")

matrix=[]
for i in range(5):
   matrix.append(r.recvuntil(b"\n"))

print(matrix)
nums=[]
cons=[]

for mm in matrix:
   nums.append(num(str(mm))[:-1])
   cons.append(num(str(mm))[-1])
   
print(nums)
print(cons)

coef = np.array(nums)

const = np.array(cons)

solution = np.linalg.solve(coef, const).astype(np.float64)
solution=np.round(solution).astype(np.int64)
solution=[bytes(str(i).encode()) for i in solution]
print(solution)

for i in range(5):
   print(r.recvuntil(b"= "))
   print(solution[i])
   r.sendline(solution[i])

r.interactive()
