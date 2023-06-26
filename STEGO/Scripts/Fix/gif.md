### Add gif header using python script

```py
buf = open('unopenable.gif', 'rb').read()
buf = b"\x47\x49\x46\x38" + buf
with open('unopenable-fix.gif', 'wb') as fd:
    fd.write(buf)
```

![image](https://github.com/ckc9759/CTF_resources/assets/95117634/9cc7140b-b368-4e34-9b70-d893c4ab08f6)
