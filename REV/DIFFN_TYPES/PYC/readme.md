### PYC

---

```py
import marshal, dis

with open("file.pyc", "rb") as file:
    file.seek(16)
    print(dis.dis(marshal.load(file)))
```

Python source file - Use online decompiler to see the actual code.
