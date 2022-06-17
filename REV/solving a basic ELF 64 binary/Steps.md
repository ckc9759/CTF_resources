### STEPS:

Let's suppose we have a file named ckc

step 1: gdb-peda ckc
step 2: gdb-peda info func / info reg
step 3: r
step 4: start
step 5: disas
step 6: b *0x0000000008001168 ( A hex code)
step 7: x/s to print the dump inside a registry stored in hex..
