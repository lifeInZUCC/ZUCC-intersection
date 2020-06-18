## 进程同步和互斥概念

### 1.指出以下非临界资源为（ ）。
|| 选项|  
|-|-|
A|变量|
B|数据结构|
C|队列|
<font color="#FF0000">D|<font color="#FF0000">纯代码|

### 2.并发进程之间（ ）。
|| 选项|  
|-|-|
A|彼此相关|
B|必须同步|
C|必须互斥|
<font color="#FF0000">D|<font color="#FF0000">可能需要同步或互斥|

### 3.进程间的互斥和同步分别表示了各进程间的（）。
|| 选项|  
|-|-|
<font color="#FF0000">A|<font color="#FF0000">竞争与协作|
B|相互独立与相互制约|
C|不同状态|
D|动态性和并发性|

## 信号量概念和PV操作

### 1.Semaphores are a convinient and effective mechanism for:
|| 选项|  
|-|-|
A|Deadlock avoidance 死锁避免|
B|Memory management存储管理|
C|Process scheduling进程调度|
<font color="#FF0000">D|<font color="#FF0000">Process synchronization进程同步|

### 2.The semaphore in an OS is __.
|| 选项|  
|-|-|
A|a process scheduler进程调度器|
B|a data section数据段|
<font color="#FF0000">C|<font color="#FF0000">a synchronization mechanism同步机制|
D|a segment of code代码段|

### 3.对于记录型信号量，在执行一次P操作时，信号量的值应当为（）；当其值为小于0时，进程应阻塞。
|| 选项|  
|-|-|
A|不变|
B|加1|
<font color="#FF0000">C|<font color="#FF0000">减1|
D|加减指定数值|

### 4.实现进程互斥时，用（）对应，对同一个信号量调用PV操作实现互斥。
|| 选项|  
|-|-|
A|一个信号量与一个临界区|
B|一个信号量与一个相关临界区|
<font color="#FF0000">C|<font color="#FF0000">一个信号量与一组相关临界区|
D|一个信号量与一个消息|

### 5.在执行V操作时，当信号量的值（）时，应释放一个等待该信号的进程。
|| 选项|  
|-|-|
A|>0|
B|<0|
C|>=0|
<font color="#FF0000">D|<font color="#FF0000"><=0|

## 信号量解决互斥/同步问题

### 1.用P，V操作可以解决进程的同步与互斥问题
|选项||
|--|--|
|<font color="#FF0000">A|<font color="#FF0000">对|
|B| 错|

### 2.设有5个进程共享一个互斥段，如果允许有3个进程同时进入互斥段，则所采用的互斥信号量的初值应是（）。
|| 选项|  
|-|-|
A|5|
<font color="#FF0000">B|<font color="#FF0000">3|
C|1|
D|0|

### 3.计算机操作系统中，有四个相关的并发进程，涉及一类临界资源。若P、V操作的信号量S初值为2，当前值为-1，则表示有（）个等待进程。
|| 选项|  
|-|-|
A|0|
<font color="#FF0000">B|<font color="#FF0000">1|
C|2|
D|3|

### 4.对两个并发进程，其互斥信号量为mutex；若mutex=0，则表明（）。
|| 选项|  
|-|-|
A|没有进程进入临界区|
<font color="#FF0000">B|<font color="#FF0000">有一个进程进入临界区但没进程处于阻塞状态|
C|一个进程进入临界区而另一个进程正处于等待进入临界区状态|
D|有两个进程进入临界区|