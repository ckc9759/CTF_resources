Question 

```cpp
#include <stdio.h>
#include <string.h>
int BOF() {
  char level[16]="guest";
  char name[16];
  printf("What is your name?\n: ");
  scanf("%s", name);
  printf("Hello, %s. Your level is %s\n", name, level);
  if(!strcmp(level, "admin")){
      printf("Congratulation!\n");
      return 0;
  }
  else{
      printf("Sorry, You have failed.\n");
      return -1;
  }
}
int main() {
   printf("Let's do BOF!\n");
   BOF();
   return 0;
}
```

Solution : 

![bff.png]()
