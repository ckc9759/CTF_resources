### File finding

---

Finding a file with a name in current working directory.
```py
find . -name <filename>
```

Find .png files inside home

```py
find /home -name *.png
```

Using Grep 

```py
grep -rnw "file path" -e 'flag'
```
```py
grep -r "flag" /backup/....

Somtimes we have a directory with a name like ckc 123, then we must specify that space while writing file path as /backup/ckc\ 123/abc folder
```

