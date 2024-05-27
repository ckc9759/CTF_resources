### Format String Vulnerability

---

`A format string vulnerability is a bug where user input is passed as the format argument to printf, scanf, or another function in that family.`

`%x.%x.%x.%x` - stack values
`%f` - float
`%p` - stack canary

```py
%c — Formats a single character
%d — Formats an integer in decimal value
%f — Formats float in decimal value
%p — Formats a pointer to address location
%s — Formats a string
%x — Formats a hexadecimal value
%n — Number of bytes written
```

