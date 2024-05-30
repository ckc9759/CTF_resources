### GPG

---

GPG uses the AES algorithm to encrypt your files - with encryption, the algorithm used has a big part to play in the speed of encrypting and decrypting, and how secure the algorithm is (certain algorithms can be cracked easily).

Example :

ENCRYPTION 

```py
gpg -c data.txt 
```

Now the data in data.txt will be scrambled and if we want to decrypt it, we need the key.

DECRYPTION
```py
gpg -d data.txt.gpg

and then enter the correct key or password
```

For data integrity, we can send the hash of our file to the receiver.

```py
┌──(ckc9759㉿Kali)-[~/Desktop]
└─$ md5sum ckc.txt
4b41e806cc025c21ac9248289c144c47  ckc.txt
```



