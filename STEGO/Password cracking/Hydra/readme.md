### Hydra

---

```py
Hydra is a brute force online password cracking program; a quick system login password 'hacking' tool.
```

#### Formats : 

---

Hydra
```py
hydra -l user -P passlist.txt ftp://192.168.0.1
```

SSH
```py
hydra -l <username> -P <full path to pass> <ip> -t 4 ssh
```

Post web form
```py
hydra -l <username> -P <password list> <ip> http-post-form "/<login url>:username=^USER^&password=^PASS^:F=incorrect" -V
```

