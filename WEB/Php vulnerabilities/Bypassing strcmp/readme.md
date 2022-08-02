### N o T e S

---

Strcmp and == is a loose comparison. 
strcmp checks if both the passwords : the actual and the one we entered are equal.
If they are equal, strcmp returns true or 0. We cannot make them equal  directly due to some conditions,
We can use an array as the password and hence, it will not be treated as a string.

```py
After a bit more research, it seemed that strcmp had some issues when comparing a string to something else.
If I set $_GET[‘password’] equal to an empty array, then strcmp would return a NULL. Due to some inherent weaknesses in PHP’s comparisons, NULL == 0 will return true
```

#### Injection :

```php
http://ctf.hackucf.org:4000/cmp/cmp.php?passwd[]=123
```

We specified the password as an array in the url and we got the flag : Warning: strcmp() expects parameter 1 to be string, array given in /var/www/html/cmp/cmp.php on line 8
flag{php_is_really_really_well_designed}
