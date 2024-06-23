### N o T e S

---

#### Py jail 

In such questions, we are given a netcat command and a source code file.

```
Python sandbox escape -
In one of the examples, we make use of builtins command to list all the files in our operating system.
After the python file works fine with the dummy flag, we use it with the server. 
The reverse slash is used to type in hex in reverse format in python like \x48\x69\x20\x69\x20\x61\x6d\x20\x63\x6b\x63.

Use a help command which is more than 1 page long such that paginator is invoked, then use :e to examine and then enter flag.txt to view the contents of the flag.
```

### Approach

1. Use bold or italics
2. Check __class__ __subclass__ __globals__ __builtins__ __init__ to know what is accesible
3. Check blacklist, whitelist and what all is allowed
4. Try payloads

[Jail1](https://sidsbits.com/jail-escapes/)  
[wapiflapi](http://wapiflapi.github.io/2013/04/22/plaidctf-pyjail-story-of-pythons-escape.html)  
[hacktricks](https://book.hacktricks.xyz/generic-methodologies-and-resources/python/bypass-python-sandboxes)  
[gynvael](https://gynvael.coldwind.pl/n/python_sandbox_escape)  

