### Walkthrough to a ctflearn challenge !!

using  `gdb-peda`

```py
ckc9759@ckc:/mnt/c/Users/Chaitanya K Chauhan/desktop/ctflearn$ gdb --args r CTFlearn{flag}
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
Reading symbols from r...
(No debugging symbols found in r)
gdb-peda$ r
Starting program: /mnt/c/Users/Chaitanya K Chauhan/Dropbox/My PC (ckc)/Desktop/ctflearn/r CTFlearn\{flag\}
Welcome to the CTFlearn Reversing Challenge Reykjavik v2: CTFlearn{flag}
Compile Options: ${CMAKE_CXX_FLAGS} -O0 -fno-stack-protector -mno-sse

Sorry Dude, 'CTFlearn{flag}' is not the flag :-(

[Inferior 1 (process 77) exited with code 04]
Warning: not running
```

```py
gdb-peda$ start
[----------------------------------registers-----------------------------------]
RAX: 0x80010a0 --> 0x54415541fa1e0ff3
RBX: 0x80012e0 --> 0x8d4c5741fa1e0ff3
RCX: 0x80012e0 --> 0x8d4c5741fa1e0ff3
RDX: 0x7ffffffee350
RSI: 0x7ffffffee338
RDI: 0x2
RBP: 0x0
RSP: 0x7ffffffee248
RIP: 0x80010a0 --> 0x54415541fa1e0ff3
R8 : 0x0
R9 : 0x7fffff7c1d60 (<_dl_fini>:        endbr64)
R10: 0x7
R11: 0x2
R12: 0x80011f0 --> 0x8949ed31fa1e0ff3
R13: 0x7ffffffee330
R14: 0x0
R15: 0x0
EFLAGS: 0x246 (carry PARITY adjust ZERO sign trap INTERRUPT direction overflow)
[-------------------------------------code-------------------------------------]
   0x8001090 <__printf_chk@plt>:        endbr64
   0x8001094 <__printf_chk@plt+4>:
    bnd jmp QWORD PTR [rip+0x2f35]        # 0x8003fd0 <__printf_chk@got.plt>
   0x800109b <__printf_chk@plt+11>:     nop    DWORD PTR [rax+rax*1+0x0]
=> 0x80010a0 <main>:    endbr64
   0x80010a4 <main+4>:  push   r13
   0x80010a6 <main+6>:  push   r12
   0x80010a8 <main+8>:  push   rbp
   0x80010a9 <main+9>:  sub    rsp,0x20
[------------------------------------stack-------------------------------------]
Invalid $SP address: 0x7ffffffee248
[------------------------------------------------------------------------------]
Legend: code, data, rodata, value

Temporary breakpoint 1, 0x00000000080010a0 in main ()
```

```py
gdb-peda$ disas
Dump of assembler code for function main:
=> 0x00000000080010a0 <+0>:     endbr64
   0x00000000080010a4 <+4>:     push   r13
   0x00000000080010a6 <+6>:     push   r12
   0x00000000080010a8 <+8>:     push   rbp
   0x00000000080010a9 <+9>:     sub    rsp,0x20
   0x00000000080010ad <+13>:    cmp    edi,0x1
   0x00000000080010b0 <+16>:    je     0x80011b5 <main+277>
   0x00000000080010b6 <+22>:    mov    rbp,QWORD PTR [rsi+0x8]
   0x00000000080010ba <+26>:    mov    edi,0x1
   0x00000000080010bf <+31>:    xor    eax,eax
   0x00000000080010c1 <+33>:    lea    rsi,[rip+0xf60]        # 0x8002028
   0x00000000080010c8 <+40>:    mov    rdx,rbp
   0x00000000080010cb <+43>:    call   0x8001090 <__printf_chk@plt>
   0x00000000080010d0 <+48>:    lea    rdi,[rip+0xf91]        # 0x8002068
   0x00000000080010d7 <+55>:    call   0x8001070 <puts@plt>
   0x00000000080010dc <+60>:    lea    rdx,[rip+0xfcd]        # 0x80020b0
   0x00000000080010e3 <+67>:    mov    ecx,0x20
   0x00000000080010e8 <+72>:    mov    rsi,rbp
   0x00000000080010eb <+75>:    mov    rdi,rdx
   0x00000000080010ee <+78>:    repz cmps BYTE PTR ds:[rsi],BYTE PTR es:[rdi]
   0x00000000080010f0 <+80>:    seta   al
   0x00000000080010f3 <+83>:    sbb    al,0x0
   0x00000000080010f5 <+85>:    test   al,al
   0x00000000080010f7 <+87>:    je     0x80011c9 <main+297>
   0x00000000080010fd <+93>:    mov    rdx,QWORD PTR [rip+0x2f0c]        # 0x8004010 <data>
   0x0000000008001104 <+100>:   mov    r13,rsp
   0x0000000008001107 <+103>:   mov    rsi,rbp
   0x000000000800110a <+106>:   mov    BYTE PTR [rsp+0x1b],0x0
   0x000000000800110f <+111>:   movabs rax,0xabababababababab
   0x0000000008001119 <+121>:   mov    rdi,r13
   0x000000000800111c <+124>:   xor    rdx,rax
   0x000000000800111f <+127>:   mov    QWORD PTR [rsp],rdx
   0x0000000008001123 <+131>:   mov    rdx,QWORD PTR [rip+0x2eee]        # 0x8004018 <data+8>
   0x000000000800112a <+138>:   xor    rdx,rax
   0x000000000800112d <+141>:   xor    rax,QWORD PTR [rip+0x2eec]        # 0x8004020 <data+16>
   0x0000000008001134 <+148>:   mov    QWORD PTR [rsp+0x10],rax
   0x0000000008001139 <+153>:   movzx  eax,BYTE PTR [rip+0x2ee8]        # 0x8004028 <data+24>
   0x0000000008001140 <+160>:   mov    QWORD PTR [rsp+0x8],rdx
   0x0000000008001145 <+165>:   xor    eax,0xffffffab
   0x0000000008001148 <+168>:   mov    BYTE PTR [rsp+0x18],al
   0x000000000800114c <+172>:   movzx  eax,BYTE PTR [rip+0x2ed6]        # 0x8004029 <data+25>
   0x0000000008001153 <+179>:   xor    eax,0xffffffab
   0x0000000008001156 <+182>:   mov    BYTE PTR [rsp+0x19],al
   0x000000000800115a <+186>:   movzx  eax,BYTE PTR [rip+0x2ec9]        # 0x800402a <data+26>
   0x0000000008001161 <+193>:   xor    eax,0xffffffab
   0x0000000008001164 <+196>:   mov    BYTE PTR [rsp+0x1a],al
   0x0000000008001168 <+200>:   call   0x8001080 <strcmp@plt>
   0x000000000800116d <+205>:   mov    r12d,eax
   0x0000000008001170 <+208>:   test   eax,eax
   0x0000000008001172 <+210>:   jne    0x8001197 <main+247>
   0x0000000008001174 <+212>:   mov    rdx,r13
   0x0000000008001177 <+215>:   lea    rsi,[rip+0xf7a]        # 0x80020f8
   0x000000000800117e <+222>:   mov    edi,0x1
   0x0000000008001183 <+227>:   xor    eax,eax
   0x0000000008001185 <+229>:   call   0x8001090 <__printf_chk@plt>
   0x000000000800118a <+234>:   add    rsp,0x20
   0x000000000800118e <+238>:   mov    eax,r12d
   0x0000000008001191 <+241>:   pop    rbp
   0x0000000008001192 <+242>:   pop    r12
   0x0000000008001194 <+244>:   pop    r13
   0x0000000008001196 <+246>:   ret
   0x0000000008001197 <+247>:   mov    rdx,rbp
   0x000000000800119a <+250>:   mov    edi,0x1
   0x000000000800119f <+255>:   xor    eax,eax
   0x00000000080011a1 <+257>:   mov    r12d,0x4
   0x00000000080011a7 <+263>:   lea    rsi,[rip+0xf7a]        # 0x8002128
   0x00000000080011ae <+270>:   call   0x8001090 <__printf_chk@plt>
   0x00000000080011b3 <+275>:   jmp    0x800118a <main+234>
   0x00000000080011b5 <+277>:   lea    rdi,[rip+0xe4c]        # 0x8002008
   0x00000000080011bc <+284>:   mov    r12d,0x1
   0x00000000080011c2 <+290>:   call   0x8001070 <puts@plt>
   0x00000000080011c7 <+295>:   jmp    0x800118a <main+234>
   0x00000000080011c9 <+297>:   lea    rsi,[rip+0xf00]        # 0x80020d0
   0x00000000080011d0 <+304>:   mov    edi,0x1
   0x00000000080011d5 <+309>:   mov    r12d,0x2
   0x00000000080011db <+315>:   call   0x8001090 <__printf_chk@plt>
   0x00000000080011e0 <+320>:   jmp    0x800118a <main+234>
End of assembler dump.
```


```py
gdb-peda$ b *0x0000000008001168
Breakpoint 2 at 0x8001168
gdb-peda$ r
Starting program: /mnt/c/Users/Chaitanya K Chauhan/Dropbox/My PC (ckc)/Desktop/ctflearn/r CTFlearn\{flag\}
Welcome to the CTFlearn Reversing Challenge Reykjavik v2: CTFlearn{flag}
Compile Options: ${CMAKE_CXX_FLAGS} -O0 -fno-stack-protector -mno-sse

[----------------------------------registers-----------------------------------]
RAX: 0xffffff7d
RBX: 0x80012e0 --> 0x8d4c5741fa1e0ff3
RCX: 0x16
RDX: 0x76304c5f6579457b ('{Eye_L0v')
RSI: 0x7ffffffee5af
RDI: 0x7ffffffee210
RBP: 0x7ffffffee5af
RSP: 0x7ffffffee210
RIP: 0x8001168 --> 0xc48941ffffff13e8
R8 : 0x47 ('G')
R9 : 0x49 ('I')
R10: 0x8002064 --> 0x706d6f430000000a ('\n')
R11: 0x8002064 --> 0x706d6f430000000a ('\n')
R12: 0x80011f0 --> 0x8949ed31fa1e0ff3
R13: 0x7ffffffee210
R14: 0x0
R15: 0x0
EFLAGS: 0x286 (carry PARITY adjust zero SIGN trap INTERRUPT direction overflow)
[-------------------------------------code-------------------------------------]
   0x800115a <main+186>:        movzx  eax,BYTE PTR [rip+0x2ec9]        # 0x800402a <data+26>
   0x8001161 <main+193>:        xor    eax,0xffffffab
   0x8001164 <main+196>:        mov    BYTE PTR [rsp+0x1a],al
=> 0x8001168 <main+200>:        call   0x8001080 <strcmp@plt>
   0x800116d <main+205>:        mov    r12d,eax
   0x8001170 <main+208>:        test   eax,eax
   0x8001172 <main+210>:        jne    0x8001197 <main+247>
   0x8001174 <main+212>:        mov    rdx,r13
No argument
[------------------------------------stack-------------------------------------]
Invalid $SP address: 0x7ffffffee210
[------------------------------------------------------------------------------]
Legend: code, data, rodata, value

Breakpoint 2, 0x0000000008001168 in main ()
gdb-peda$ x/s 0x7ffffffee210
0x7ffffffee210: "CTFlearn{Eye_L0ve_Iceland_}"
gdb-peda$ x/s 0x7ffffffee210
0x7ffffffee210: "CTFlearn{Eye_L0ve_Iceland_}"
```
