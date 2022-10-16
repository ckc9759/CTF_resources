### N o T e S

---

## SSH - Secure Shell

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

Important directories : 

```
/etc -- System files
/etc/passwd -- passwords stored 
/etc/shadow -- sha512 hash passwd
/var -- variable data
/root -- root user info and data
/tmp -- temporary data
```

#### Nth position on a list

```cpp
sed -n 148p /home/santa/naughty_list.txt 
```

### /opt

```py
Sometimes the directories in ssh aren't accessible directly as we don't have root permision.
In that case, we can just use sudo -l to view the permissions.
In my case, i found an opt directory with reader in it which didn't require any permissions to run
```


