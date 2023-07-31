### Blacklist Payloads

---

```py
del blacklist[:]
```

```py
1. Use unicode look-alikes if input is not filtered to ascii.
2. Vuln of eval function
```

### Filters in character or ascii

```py
1. Use the module itself, eg: __builtins__.print
2. If you have to call a function and something is filtered, then try taking it inside another one and use the function as string
Eg : vars(vars()['__buil'+chr(116)+'ins__'])['prin'+chr(116)](_)
```

### Filters in numbers

```py
Tadpole operators to add or subtract :
-~y	y + 1	Tadpole swimming toward a value makes it bigger
~-y	y - 1	Tadpole swimming away from a value makes it smaller
```

### Filters in parantheses and special characters '.,-\*'

```py
Use errors and whatever characters are unfiltered.
[_==_][_!=_] --> [True][False]
