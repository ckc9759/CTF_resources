Useful links :

https://ctftime.org/writeup/31187  
https://ctftime.org/writeup/23809  
https://github.com/Dvd848/CTFs/blob/master/2019_picoCTF/c0rrupt.md
[zsteg-mask](https://medium.com/@cyDeer/bobby-toes-ipad-ctf-walkthrough-0118a8879b93)

---

### Xor two images

```py
convert crypted1.png crypted2.png -fx "(((255*u)&(255*(1-v)))|((255*(1-u))&(255*v)))/255" decrypted.png
```
