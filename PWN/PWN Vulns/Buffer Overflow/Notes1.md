### N o T e S

---

```bash
readelf - It is a command which is used to look at the type of variables : global local or a function of an ELF file.

readelf -s <binary file name>  | grep -i "FUNC"
```

```
dmesg | tail --> It is used to find the address at which the ELF file encountered a segmentation fault and it's core was dumped.
```

Firstly, after idenitfying that the ELF has buffer overflow vulnerability in it, we need to find the offset after which we can point to the memory address we want for the flag.

So, we can either use python printing A's and using binary search to find the offset or we can use the cyclic tool of pwn to identify the offset.

Once, we know the offset we can control the memory address by concatenating the address in bytes after the required number of A's.

We use dmesg every time to find the offset where we will encounter sef fault for the first time. Then, we can concatenate the string with the memory address of the function we wish to execute.

#### Example :

```py
python -c "print('A'*32 + '\x82\x40\x08\x3b')" | ./program
```

---

Thank you
