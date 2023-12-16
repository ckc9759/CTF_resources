### NOTES

---

Vuln in

```php
include $_GET['file'];
```
or
```php
include $_GET['file'] . ".php";
```
