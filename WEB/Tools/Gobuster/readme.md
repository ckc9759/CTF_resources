### Gobuster

---

```py
gobuster dir -u <website address> -w <wordlist.txt>
```

### Subdomain enumeration

```linux
gobuster vhost -w /opt/useful/SecLists/Discovery/DNS/subdomains-top1million-5000.txt -u http://thetoppers.htb

-w Wordlist -u URL

ffuf -c -w /usr/share/wordlists/dirbuster/directory-list-2.3-small.txt -u http://thetoppers.htb -H "Host:FUZZ.thetoppers.htb" -fs 11952

```

### Files

```linux
-x --> specify files to look for
```
