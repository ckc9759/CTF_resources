### All about RSA 
---
RSA Encryption
---

Also known as Rivest-Shamir-Adleman

- It is a kind of assymetric cryptography.
- Modular arithmetics (exponentiation)
- The most widely used public-key cryptosystem.

Useful links: http://factordb.com/


Generally in such CTF challenges, we are given `n` `e` and `c` in the challenge.

#### `e` is the public key...

```python
n is a modulus which is calculated using:
n=p*q
It is a link between public and private keys.
```

Then we have two more factors which is `p` and `q`.
---
When we have unknown p and q, we use this theory
```python
Let A=(p+q)/2 , i.e., A is mid point of p and q, which could be nearer to N−−√

There exist an integer x so that, A−x=p and A+x=q

N=pq = (A−x)(A+x)=A2−x2

x=A2−N−−−−−−√

Since we know A and N we can find x and subsequently p and q.
```

With the help of p and q, we calculate phi.

```python
phi=(p-1)*(q-1)
Euler's Totient function
```
The last parameter left is `d`.

for `d` which is the **private key** , we need some scripting.

```python
from Crypto.Util.number import inverse
d=inverse(e,phi)
print(d)
```
For the parameter `m`, we do 
```python
m=pow(c,d,n)
print (hex(m)[2:-1].decode('hex'))
```

This gives us the flag in general cases.

### NOTE:
---
The trick with RSA is that `e` and `d` are related such that you can encrypt with either one and then decrypt it with the other.
For actual encryption you encrypt with the public key, so the private key is required for decryption.
But you can also "encrypt" it with your private key to sign the message - then everyone can "decrypt" it with your public key which verifies it was actually you who sent it.

Sometime, we are given `s` which stands for signature. In such cases, if we have `s`, `e` and `n` we can find the flag,
Eg:
```py
from Crypto.Util.number import *
s = 6747770137526404810839680591618349902868945426501581276399132116507818856417271976886226143238796548185022079396435297411063351895882402872038955136430497260880818613647851713479263986391308789043197324119239260033630040630976512064481721240642729114116561261667588426398515959668695454587899042998666589705506998832917739337175589667828567571421541128057015371328723095841794613223799998429126797512729366352049800447550388154359724453576012916007310993864290045596969157854816882402679820492333445924724199994952395214639223249892224753494733720946542351810699104265693993026233289328344375145590992008664182919067

e = 65537 # found from chall.py

n = 22964326243465188806208175092817347325223751455203934839482603060029805229708465878030254819573089332477084079330445929855173787412006349904864930449245982063200060526847746608051441362052994064461426109292644943462306467765210530381760387813568149905672759271878822092979239650360475796179311415340966347044401497301347973838444826544061998479163636946750265778097717211762208385963205388216125639236403616607313423716206061201112615302831337395011064188536794425701313580122604533837935452384701344503773605128479669035610395170026350607423780797383865621285538151344219282466601404674101508588637419153433890102137
print(long_to_bytes(pow(s,e,n)))

```
Flag  - n00bz{pl34s3_s1gn_h3r3_4nd_h3r3_4nd_h3r3...}

```py
>>> from Crypto.Util.number import *
>>> n=245841236512478852752909734912575581815967630033049838269083
>>> e=3
>>> c=219878849218803628752496734037301843801487889344508611639028
>>> p=416064700201658306196320137931
>>> q=590872612825179551336102196593
>>> phi=(p-1)*(q-1)
>>> d=inverse(e,phi)
>>> m=pow(c,d,n)
>>> print(hex(m)[2:-1].decode("hex")) or
>>> print(long_to_bytes(m)) or bytes.fromhex(hex(m)[2:])
```

If the last step does not work, convert the decimal to hexa and them hexa to ascii. SiMPLE..

