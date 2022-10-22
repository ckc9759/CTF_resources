Sometimes, we get flag when we change the user agent.

```py
import requests

headers = {'User-Agent':'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'}
r=requests.get("http://2018shell1.ckc.com:53383/flag", headers=headers)

print r.text
```
