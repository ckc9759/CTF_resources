IF the n given is a known one from the database then we can use this attack

```py
n= 3240340324348240233
p=3804273792473893
q=239483048902
e=65537
c=347230470394311
phi=(p-1)*(q-1)
d=inverse(e,phi)
m=pow(c,d,n)
print(long_to_bytes(m))
```
