### 1.父进程用i=fork()函数创建子进程后，子进程返回的i值是（）。
|编号|选项|
|:-|:-|
|<font color="red">A</font>|<font color="red">0</font>|
|B|1|
|C|子进程的pid值|
|D|没有返回值|

### 2.Which system call creates a new process? 
|编号|选项|
|:-|:-|
|A|read|
|<font color="red">B</font>|<font color="red">fork</font>|
|C|create|
|D|exec|

### 3.下述代码运行后，共产生（）个进程，输出（）个字符'a'。
```cpp
#include <stdio.h>
#include <sys/types.h> 
#include <unistd.h> 
int main(void)
{
    int i；
    for(i=0; i<2; i++)
    {
        fork();
        printf("a");
    }
    wait(NULL); 
    wait(NULL);
    return 0;
}
```

|编号|选项|
|:-|:-|
|A|2,2|
|B|3,4|
|C|4,6|
|<font color="red">D</font>|<font color="red">4,8</font>|

### 3.下述代码运行后，共产生（）个进程，输出（）个字符'a'。
```cpp
#include <stdio.h>
#include <sys/types.h> 
#include <unistd.h> 
int main(void)
{
    int i；
    for(i=0; i<2; i++)
    {
        fork();
        printf("a\n");
    }
    wait(NULL); 
    wait(NULL);
    return 0;
}
```

|编号|选项|
|:-|:-|
|A|2,2|
|B|3,4|
|<font color="red">C</font>|<font color="red">4,6</font>|
|D|4,8|