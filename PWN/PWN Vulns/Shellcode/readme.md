### N o T e S

---

A shellcode is used when we don't have any interesting function to print the flag for us, so we inject our own code to trick the server to print the flag or escalate privilege. A shellcode in hacking is a small piece of code used as a payload in the exploitation of a vulnerability.
It is called a shell code as it typically starts a command shell from which the attacker can control the compromised machine.

![image](https://github.com/ckc9759/CTF_resources/assets/95117634/064ba5c1-48cf-430e-97e9-6bf21274537b)

```py
Finding the offset | cyclic 100
See the EIP register value
cyclic -l <value>
NX disabled,
jump to ESP and start executing the malicious code.
ropper --file <filename> --search "jmp esp"

Use shellcraft to construct the shell code
```

Python shell code example :

```py
import pwn
pwn.asm('push 0x08048540; ret')

Output --> b'h@\x85\x04\x08\xc3'
```

Now we can use this shellcode and supply it as input for the ELF file.

---

#### Injecting shellcode



