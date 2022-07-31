### N o T e s

```php
Sometimes, we are given a php file in the source code.
It checks for a particular string after using preg_replace and if they are equal, we get our flag.

In such questions, we need to just input a double string.

For example, if preg_replace func converts a particular string to "" (blank) , we can just manipulate the string.

Req. string --> Hello
Input for preg_replace --> HeHellollo (Hello will be replaced and the rest of the string will be concatenated.
```


```php


```
