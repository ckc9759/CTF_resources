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

- ### Type Errors / Type Juggling

```php
It includes vulnerabilites such as `is_string` where we can pass a command as a string even an array etc.
Type juggling is another (similar) vulnerability where comparisons are made with == instead of ===, and automatic type conversion occurs. This can lead to exploitable bugs within the application.

Injection example - http://52.10.107.64:8001/?name[]=a&password[]=b

```

- ### Object Unserialization Injection

```php



