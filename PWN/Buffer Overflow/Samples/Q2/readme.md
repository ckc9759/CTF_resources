Question

```c
#include <stdio.h>

void secret(){
    printf("This is secret function!\n");
}

int main() {
   char name[16];
   printf("secret()'s addr: %p\n", &secret);
   printf("What is your name?\n: ");
   scanf("%s", name);
   printf("Good bye, %s.\n", name);
   return 0;
}
```

Soltuion

