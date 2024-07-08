### STEPS:

Let's suppose we have a file named ckc

```py
step 1: gdb-peda ckc
step 2: gdb-peda info func / info reg
step 3: r
step 4: start
step 5: disas
step 6: b *0x0000000008001168 ( A hex code)
step 7: x/s to print the dump inside a registry stored in hex..
```

### Imp. commands

`Disassembly analysis`  
`gdb disassemble`  
`use string to check for any leads`  
`gdb info registers`  
`gdb info functions`  
`ltrace`  
`strace`  
`nm <filename>`  
`readelf -a <filename>`  
`gdb l displays the code`  
`nm -d <file>`  
`ltrace -i -c <file>`  
`objdump -D -M <file>`  
`gdb b to create a breakpoint`  
`gdb x/s memory address`  
`disas main`     
`ni`  
`r2 - <filename>`  
`pd main / pdf main`  
`pdf @main`  
`aaa`  
`afl`  
`px @register name`  
`db hex code -- create a breakpoint`  
`ood  ?---> help`  
