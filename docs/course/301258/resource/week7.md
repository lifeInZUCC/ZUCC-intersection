## 死锁概念

### 1.系统产生死锁是指（）。
|编号|选项|
|:-|:-|
|A|系统发生重大故障|
|B|若干进程正在等待永远不可能得到的资源|
|C|请求的资源数大于系统提供的资源数|
|<font color="red">D|<font color="red">若干进程等待被其他进程所占用而又不可能被释放的资源|

### 2.如果系统在所有进程运行前，一次性地其在整个运行过程中所需地全部资源分配给进程，即所谓“静态分配”，可以预防死锁发生。
|编号|选项|
|:-|:-|
|<font color="red">A|<font color="red">对|
|B|错|

### 3.以下关于死锁的必要条件的叙述中错误的是（）。
|编号|选项|
|:-|:-|
|<font color="red">A|<font color="red">只要具备了死锁的必要条件，就一定发生死锁现象|
|B|解决死锁问题可以从死锁的必要条件出发|
|C|一旦出现死锁现象，处于死锁状态的进程一定同时具备死锁的必要条件|
|D|死锁的四个必要条件之间不是完全独立的，但也不是等价的|

### 4.死锁现象并不是计算机系统独有的，在下面例子中，除（）之外，其他三种案例都是死锁的体现。
|编号|选项|
|:-|:-|
|A|杭州西冷桥塞车，因为大修，桥上只有一个车道通行|
|<font color="red">B|<font color="red">高速公路大堵车，因为桥被台风吹垮了|
|C|两列相向行驶的列车在单轨铁路线上迎面相遇|
|D|两位木匠订地板，一位只握一把榔头，而另一位没有榔头，却有钉子|

### 5.多个进程竞争比经常数目少的资源就可能产生死锁，而当资源数目大于进程数目时就一定不会发生死锁。
|编号|选项|
|:-|:-|
|A|对|
|<font color="red">B|<font color="red">错|

## 死锁避免和检测

### 1.当同时需要用两个互斥信号量时，总是让它们以交错的顺序加锁，以避免死锁。
|编号|选项|
|:-|:-|
|A|对|
|<font color="red">B|<font color="red">错|

### 2.Banker's algorithm is one of __ algorithm.
|编号|选项|
|:-|:-|
|A|deadlock recovery死锁恢复|
|<font color="red">B|<font color="red">deadlock avoidance死锁避免|
|C|deadlock prevention死锁预防|
|D|deadlock detection死锁检测|

### 3.How does the Linux system deal with the deadlock?
|编号|选项|
|:-|:-|
|A|By deadlock prevention死锁预防|
|B|By deadlock avoidance死锁避免|
|C|By deadlock detection死锁检测|
|<font color="red">D|<font color="red">Do nothing|

### 4.If system use the banker's algorithm to avoid deadlock, which of the statement is correct?
|编号|选项|
|:-|:-|
|A|If the system is in an unsafe state, it must cause a deadlock.|
|<font color="red">B|<font color="red">If the system is in an unsafe state, it may cause a deadlock.|
|C|If the system is in a safe state, it may cause a deadlock.|
|D|If the system is in a safe state, it must cause a deadlock.|

### 5.There are N processes which share M mutual exclusive resources, each process can hold W resources at most. Which of the following condition may cause a deadlock?
|编号|选项|
|:-|:-|
|A|M=2, N=1, W=2|
|B|M=2, N=2, W=1|
|C|M=4, N=3, W=2|
|<font color="red">D|<font color="red">M=4, N=2, W=3|

