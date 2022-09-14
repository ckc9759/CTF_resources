### Nmap

---

***Network Scanning*** - Network connections are made between two ports – an open port listening on the server and a randomly selected port on your own computer. For example, when you connect to a web page, your computer may open port 49534 to connect to the server’s port 443.

- Every computer has a total of 65535 available ports
- Nmap is a command line tool




Nmap is used for network scanning.

```py
nmap -sC -sV 10.10.221.212
```

Directory bruteforce on a website

```py
dirb http://10.10.10.10
```

Directory bruteforce for particular files 

```py
dirb http://19.12.13.162 -X .php
```

#### Nmap Useful Switches 

```py
-p- -> all port scan 
-p -> specify port
-sU -> UDP scan
-sT -> TCP scan
activate script -> --script
```


