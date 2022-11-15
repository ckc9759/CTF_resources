### SSH Connect

```py
Sometimes, when we connect to a remote server using ssh, we don't have access to each and every file as we may not be the root user.
In such cases, it is possible that there is certain pvt key perhaps a rsa key which can be accessible by every user. 
We can use this vulnerability to read private files of the root user. 
We need to bruteforce the password for the user and then we can enter as root using pvt key to read the confidential files.

THIS PROCESS IS CALLED PRIVILEGE ESCALATION
```
