Server-Side Request forgery

Example:

- It can be used when a web app is making a request on our behalf.

```py
from flask import Flask

app=Flask(__name__)

@app.route("/")
def hello_world():
   return "<p>Hello</p>"
```
![image](https://github.com/ckc9759/CTF_resources/assets/95117634/67b57ed0-e4e7-493d-b75d-89f86da4a5b0)

