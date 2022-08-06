### N o T e S

---

Example : 

Connecting to a server with username ckc1404 and password ckc3.

Server name --> ckc.lab.org 
Port --> 9759

ssh ckc1404@ckc.lab.org -p 9759

---

Finding a file with certain size and property.

Example size 256 bytes and not executable

--> `find -type f -size 256c ! -executable`

---

Finding a user with name bandit7, group bandit6 and size 33 bytes.

```py
find / -user bandit7 -group bandit6 -size 33c 2>&1 | grep -F -v Permission | grep -F -v directory
```

---

To check if a line is ocurred only once i.e unique.

```py
cat data.txt | sort | uniq -c -u
```

---

