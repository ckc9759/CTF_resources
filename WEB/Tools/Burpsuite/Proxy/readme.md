### Proxy

---

This is one of the most useful tab of Burpsuite !!!

If you want to view the request a website requests in order to show a response, we can use the proxy tab of Burpsuite. 
Turn on the intercept and open the website in Burp browser. 

We will get the requests that the website wants.


#### Example

```py
GET /header.php HTTP/1.1
Host: 165.227.106.113
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5304.107 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9
Connection: close
```


