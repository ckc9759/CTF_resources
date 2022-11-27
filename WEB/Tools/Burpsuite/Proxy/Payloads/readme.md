### { Payloads }

---

```py
User-Agent: Ckc # To change the user agent of the website
```

```py
Referer: ckc.com # To change the intial point of the website as if the user is coming from ckc.com
```

```py
GET / HTTP/1.1
Host: mercury.picoctf.net:34588
Upgrade-Insecure-Requests: 1
User-Agent:PicoBrowser # User agent
Referer:http://mercury.picoctf.net:34588/ # To specify the site from where we r coming
Date: Wed, 21 Oct 2018 07:28:00 GMT # To specify the date
DNT:1 # To avoid being tracked (DO NOT TRACK Header)
X-Forwarded-For: 31.3.152.55 # To change the location to sweden using a sweden IP
Accept-Language: sv,en;q=0.9 # To change the language to sweden in this case
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9
Connection: close
```
