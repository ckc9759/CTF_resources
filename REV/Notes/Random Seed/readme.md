### Random

---

```cpp
#include <stdlib.h>

int win(){
    int fd = open("./flag.txt",0);
    sendfile(1,fd,0,100);
    exit(0);
}

int main() {
    srand(time(0));
    int rand_num;
    int user_num;
    
    printf("Give me a number: ");
    scanf("%d", &user_num);
    
    rand_num = rand();
    
    if (rand_num == user_num) {
        printf("Correct \n ");
        win();
    }
    
    printf("Wrong!\n");
    printf("I randomly generated:\n%d", rand_num);
}
```

---

Exploit : 

```cpp
echo "test" | ./re | sed -n 3p | ./re
```
