### Radare

---

```py
r2 -d -A chall

-d : run the ELF
-A : Analysis
```

```py
s main; pdf (Dissamble the main program)

s main --> seeks main
pdf --> Print Disassembly Function
```

```py
db 0x01b66179 ( breakpoint at a particular address)

db --> debug breakpoint
A breakpoint is simply somewhere which, when reached, pauses the program for you to run other commands.

Now we run dc for debug continue; this just carries on running the file.
```

```py
pwx @esp --> it returns the address and value of esp register

ds --> debug step, moves one step down
```




