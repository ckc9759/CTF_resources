from Crypto.Util.number import *
from sympy import root
from sympy.ntheory.modular import crt
n1 = 86812553978993
n2 = 81744303091421 
n3 = 83695120256591
c1 = 8875674977048
c2 = 70744354709710
c3 = 29146719498409
m = int(root(crt([n1,n2,n3],[c1,c2,c3])[0],3))
print(m)
