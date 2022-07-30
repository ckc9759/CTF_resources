### N o T e S

---

- ### SQL Injection
```php
<?php
    $username = $_GET['username']; // kchung
    $result = mysql_query("SELECT * FROM users WHERE username='$username'");
?>
```


- ### RFI / LFI

```php
Remote file Inclusion and Local file Inclusion
Any time code uses include, fopen, file_get_contents, file_put_contents, require_once or a whole host of other functions, it is potentially vulnerable!
```

```php
<?php
if (isset($_GET['language'])) {
    include($_GET['language'] . '.php');
}
?>
```

---

- ### 
