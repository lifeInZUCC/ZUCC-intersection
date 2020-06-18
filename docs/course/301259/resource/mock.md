## 判断题
### 1.当同时需要用两个互斥信号量时，总是让它们以交错的顺序加锁，以避免死锁。
|编号|选项|
|:-|:-|
|A|T|
|<font color="red">B</font>|<font color="red">F</font>|

### 2.由signal（）注册的信号只是用来通知某进程发生了什么事件，并不给该进程传递任何数据。
|编号|选项|
|:-|:-|
|<font color="red">A</font>|<font color="red">T</font>|
|B|F|

### 3.共享内存允许两个或多个进程共享一给定的存储区，因为数据不需要来回复制，所以是最快的一种进程间通信机制。
|编号|选项|
|:-|:-|
|<font color="red">A</font>|<font color="red">T</font>|
|B|F|

### 4.Linux系统中的文件名不区分大小写。
|编号|选项|
|:-|:-|
|A|T|
|<font color="red">B</font>|<font color="red">F</font>|

### 5.进程的所有信息对该进程的所有线程都是共享的，包括可执行的程序文本、程序的全局内存和堆内存、栈以及文件描述符。
|编号|选项|
|:-|:-|
|<font color="red">A</font>|<font color="red">T</font>|
|B|F|

## 选择题
### 1.用户向操作系统提出服务请求一般有两种方式：终端命令和(  )。
|编号|选项|
|:-|:-|
|<font color="red">A</font>|<font color="red">系统调用</font>|
|B|高级语言|
|C|宏命令|
|D|汇编语言|

### 2.操作系统中提及的信号量（semaphore）是（   ）。
|编号|选项|
|:-|:-|
|A|进程调度分派器|
|B|代码段|
|<font color="red">C</font>|<font color="red">进程同步机制</font>|
|D|数据段|

### 3.下述代码运行后，共产生（  )个进程，输出（  ）个字符‘a' 。

```c
#include<stdio.h>
#include<sys/types.h>
#include<unistd.h>

int main()
{
	int i;
	for(i = 0; i < 2; i++)
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
|A|2，2|
|B|3，4|
|C|4，6|
|<font color="red">D</font>|<font color="red">4，8</font>|

### 4.在Linux环境执行“gcc hello.c”，将产生__ 。
|编号|选项|
|:-|:-|
|A|hello.o|
|B|hello|
|<font color="red">C</font>|<font color="red">a.out</font>|
|D|hello.exe|

### 5.Linux命令的一般格式是：
|编号|选项|
|:-|:-|
|<font color="red">A</font>|<font color="red">命令名 [选项] [参数]</font>|
|B|[选项] [参数] 命令名|
|C|[参数] [选项] 命令名|
|D|[命令名] [选项] [参数]|

## 填空题

1.下述程序实现父子进程间通过信号异步通信：子进程在等待5秒后用系统调用kill（）向父进程发送SIGALARM信号，父进程用系统调用signal( )捕捉SIGLARM信号。

```c
#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <signal.h>
static int alarm_fired = 0;            //闹钟未设置

void ding(int sig)          //模拟闹钟
{
	alarm_fired = 1;               //设置闹钟
}

int main()
{
	int pid;

	printf("alarm application starting\n");
	if((pid = fork( )) == 0) 
	{     
		sleep(5);                //子进程5秒后发送信号SIGALRM给父进程
		kill(getppid(), 16);
		exit(0);
	}
//父进程安排好捕捉到SIGALRM信号后执行ding函数
	printf("waiting for alarm to go off\n");
	(void) signal(16, ding); 
	pause();           //挂起父进程，直到有一个信号出现
	wait(0);
	if (alarm_fired)
		printf("Ding!\n");
	printf("done\n");
	exit(0);
}
```

2.Linux内核源代码中，`/ipc`目录包含了核心进程间的通信代码。

3.生产围棋的工人不小心把相等数量的黑子和白子混装于一个箱子里，现要用自动分拣系统把黑子和白子分开。 该系统由两个并发执行的线程组成，功能如下：(1) 线程 A专门拣黑子， 线程 B专门拣白子；(2)每个线程每次只拣一个子，要求并发线程交替拣子。试用信号量操作实现两者的互斥同步。

```c
#include <pthread.h>
#include <semaphore.h>
#include <sys/types.h>
#include <stdio.h>
#include <unistd.h>

int number; // 被保护的全局变量
sem_t sem_id1, sem_id2;

void* thread_white_fun(void *arg)
{
	   int i;	
	   for(i = 0;i < 3;i++)
	   {
              sem_wait(&sem_id1);
              printf("thread_white have the semaphore\n");
              number++;
              printf("number = %d\n",number);
              sem_post(&sem_id2);
		}	
}
void* thread_black_fun(void *arg)
{
	int i;	
	for(i = 0;i < 3;i++)
		{
			sem_wait(&sem_id2);
			printf("thread_black have the semaphore \n");
			number--;
			printf("number = %d\n",number);
			sem_post(&sem_id1);
		}
	
}
int main(int argc,char *argv[])
{
	number = 0;
	pthread_t id1, id2;
	sem_init(&sem_id1, 0, 1); // 空闲的
	sem_init(&sem_id2, 0, 0); // 忙的
	
    pthread_create(&id1,NULL,thread_white_fun, NULL);
	pthread_create(&id2,NULL,thread_black_fun, NULL);
	pthread_join(id1,NULL);
	pthread_join(id2,NULL);
	printf("main\n");
	return 0;
}
```

4.`Makefile`文件是用来告诉make命令如何编译和链接程序。

5.用`top`命令动态显示当前系统正在执行的进程的相关信息，包括进程ID、内存占用率、CPU占用率等，该命令默认3s刷新一次。

6.GCC编译器有许多选项，其中-`o`选项要求输出可执行文件名。