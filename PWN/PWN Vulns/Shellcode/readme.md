### N o T e S

---

A shellcode in hacking is a small piece of code used as a payload in the exploitation of a vulnerability.
It is called a shell code as it typically starts a command shell from which the attacker can control the compromised machine.

Python shell code example :

```py
import pwn
pwn.asm('push 0x08048540; ret')

Output --> b'h@\x85\x04\x08\xc3'
```

Now we can use this shellcode and supply it as input for the ELF file.

---

#### Injecting shellcode



