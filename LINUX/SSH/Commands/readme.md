## Commands

---

### Finding a particular string from a list of files

Searching for string ckc from all files in downloads directory

```py
grep "ckc" /home/downloads *
```

Searching only the txt files for string ckc

```py
grep "ckc" /home/downloads *.txt
```

### Listing users on a ssh system

```py
cat /etc/passwd
```

#### Users who can log into the ssh machine

```py
cat /etc/passwd | grep "/bin/bash" | wc -l
```

#### Sha1 hash of a file

```py
sha1sum filename
```

### Passwords :

```py
Stored in /cat/shadow

cat /cat/shadow | grep -i "any string in password"
```

### Environment variables

```py
env command
```

---

## Finding a file (let's say abc)

```py
where abc
locate abc

or find / -name abc
```






