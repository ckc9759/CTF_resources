### Format String Vulnerability

---

`A format string vulnerability is a bug where user input is passed as the format argument to printf, scanf, or another function in that family.` The stack values are leaked if the number of parameters expected by printf etc is less than format string specifiers.

`%x.%x.%x.%x` - stack values
`%f` - float
`%p` - stack canary
`%6$p` - 6th loc of stack

```py
%c — Formats a single character
%d — Formats an integer in decimal value
%f — Formats float in decimal value
%p — Formats a pointer to address location
%s — Formats a string
%x — Formats a hexadecimal value
%n — Number of bytes written
```

Below are some format parameters which can be used and their consequences:

•”%x” Read data from the stack
•”%s” Read character strings from the process’ memory
•”%n” Write an integer to locations in the process’ memory

[owasp](https://owasp.org/www-community/attacks/Format_string_attack)
[liveoverflow](https://www.youtube.com/watch?v=0WvrSfcdq1I)

STEPS

1. Find the offset with experimenting - spam a long %x and look for the first repeating occurence, that gives you the offset..
Test it with aaabbb.....%{n}$x

[ROP chain](https://github.com/ckc9759/CTF_resources/tree/main/PWN/Scripts/Format%20String)

