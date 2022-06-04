### Imp Guidelines to approach pwn questions.


Useful commands
```python
gdb -peda command
pd main
1. To create a breakpoint in gdb peda use b* (hex value like 0x000000004011ca.
checksec --file <filename? command- It checks for the securities applied to the Binary.

2. If stack is not canary it hints towards buffer overflow.
info func for info of functions.




* Puts() statement - used to store or write something in stream. 
* Gets() statement- gives us the vulnerability as it take arbitrary input.A vulnerability function which takes input irrespective of it's size and hence has a potential overflow.
* Strcmp() statement - It is used to compare two strings.
* Strlen() - Length of string.

```

```javascript
x/s - displays the argument to a hex value like x/s 0x40772

```
