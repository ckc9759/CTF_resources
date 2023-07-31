### Blacklist Payloads

---

```
del blacklist[:]
```

```
1. Use unicode look-alikes if input is not filtered to ascii.
2. Vuln of eval function
```

### Filters in character or ascii

```
1. Use the module itself, eg: __builtins__.print
2. If you have to call a function and something is filtered, then try taking it inside another one and use the function as string
Eg : vars(vars()['__buil'+chr(116)+'ins__'])['prin'+chr(116)](_)
```
