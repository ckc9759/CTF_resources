### N o T e S

---

```py
It is not possible for two non-equal entities to have same SHA1 hash.
Also it is to be noted that there is a strict comparison (===) not a loose one.
(so our 0e trick will not work here). 
The values (name and password) are being entered through GET request parameter.
Hence we can control the value as well as the type of the variable.
If we send variables (name and password) of type array then we can bypass the SHA1 check.
As that SHA1 check will only be executed if the type of the variables (name and password) is string.
Remember strict comparison checks for both type and value, and if the type doesnt matches then
It will simply ignore the condition and we will get our flag.
```

#### Injection --> `http://vulnerable/?name[]=x&password[]=y`

