### John the ripper

---

```py
zip2john <name of zip>.zip > steg.hash
  
john --wordlist=rockyou.txt steg.hash
```

```py
7z2john flag.7z > steg.hash
```

#### Breaking the nthash

```py
john --format=NT --rules -w=/usr/share/wordlists/rockyou.txt hash.txt
```
