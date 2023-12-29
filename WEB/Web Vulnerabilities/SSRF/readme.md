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
