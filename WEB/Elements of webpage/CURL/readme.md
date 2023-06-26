### CURL

To send a host in the web server

```php
curl -H "HOST: ckc" http://ckc.com
```

```php
curl -I HEAD -i http://mercury.picoctf.net:64944/
```

-H is used to provide an additional request to our request.

```php
curl chall.battlectf.online:8081 -H "DNT: 1" -H "Referer: battlectf.online" -H "Client-IP: 127.0.0.1" -H "X-Forwarded-For: 127.0.0.1" -H "User-Agent: africa"
```
