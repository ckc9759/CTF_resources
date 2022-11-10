### Using burpsuite.

Open burpsuite and go to proxy and keep intercept on. That way you can see the https

It is a framework written in Java that is helpful in web application penetration testing.

```py
APIs - Application Programming Interfaces.
```

Components :

```py
Proxy - Intercept and modify requests (ctrl+shift+p)
Repeater - Capture, modify and resend requests multiple times. (ctrl+shift+r)
Intruder - Bruteforce attacks and to fuzz endpoints.(ctrl+shift+i)
Decoder - Decoding or encoding a payload or information. (dashboard --> ctrl+shift+d)
Comparer - Compare two pieces of data.
Sequencer - Accessing the randomness of cookies
```

---

#### Burp Proxy :

If we make a request to a website say https://ckc.com through Burp proxy, then our request will be captured and won't be allowed to continue to the server until we explicitly allow it through.
