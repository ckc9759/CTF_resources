### N o T e S

---

Code : 

```php
<?php
$var1=1;
$var2=1.0;
$var3="chaitanya";
$var4=true;
?>
```

- In php, we don't need to specify the type of variables.
- Type Juggling is not a vulnerability or flaw,rather it is a feature of php.
- PHP is a loosely typed language, and hence, capable of taking the data type of the value, as that of the variable, to which that value is assigned.

```py
* there are two types of comparison in php , loose comparison(== / !=) and strict comparison (=== / !==) . 
```

### Example of using type juggling and loose comparison 

```py
However it seems impossible as md5 hashes are of 16bytes (32 bytes if you hexlify them),
In short practically they can never be 0. 
If we look closely at the source code we can see that that there is a loose comparison (==) between the md5 hash and 0.
(In loose comparison only value is checked not the type of the variable).
We can exploit this comparison to print our win message.
So somehow we need to find a value whose md5 hash starts with 0e (e is exponential operator in php) then the whole md5 hash will be treated as 0.
(all thanks to type juggling and php loose comparison). 
240610708 has its md5 hash starting with 0e , hence we can set passwd variable to 240610708 , then our win message will be printed.
```

---

### Example of injection for md4 hash loose comparison

```php
plaintext :  0e001233333333333334557778889
md4 hash  :  0e434041524824285414215559233446
```


