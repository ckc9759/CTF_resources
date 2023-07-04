### Gobuster

---

```py
gobuster dir -u <website address> -w <wordlist.txt>
```

### Subdomain enumeration

```linux
gobuster vhost -w /opt/useful/SecLists/Discovery/DNS/subdomains-top1million-5000.txt -u http://thetoppers.htb

-w Wordlist -u URL
```
