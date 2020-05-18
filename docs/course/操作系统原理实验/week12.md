### 1.一般在一个进程中先用pipe创建管道，再由fork创建子进程，然后通过管道，再有fork创建子进程，然后通过管道实现父子进程间的通信。
|编号|选项|
|:-|:-|
|<font color="red">A</font>|<font color="red">对</font>|
|B|错|

### 2.下列关于管道（Pipe）通信的叙述中，正确的是（）。
|编号|选项|
|:-|:-|
|A|一个管道可实现双向数据传输|
|B|管道的容量仅受磁盘容量大小限制|
|<font color="red">C</font>|<font color="red">进程对管道进行读操作和写操作都可能被阻塞</font>|
|D|一个管道只能有一个读进程或一个写进程对其操作|

### 3.系统调用pipe()的输入参数是__。
|编号|选项|
|:-|:-|
|A|连接该管道的进程的PID号|
|B|一个整型数，表示管道的句柄；另一个整型数，表示管道的容量|
|<font color="red">C</font>|<font color="red">一个数组指针，该数组含两个整型数</font>|
|D|pipe()与fork()一样，不需要输入参数|

### 4.Linux系统中，文件描述符1表示__。
|编号|选项|
|:-|:-|
|A|管道文件描述符|
|B|标准错误输出设备文件描述符|
|C|标准输入设备文件描述符|
|<font color="red">D</font>|<font color="red">标准输出设备文件描述符</font>|

### 5.管道拥有如下特点：
|编号|选项|
|:-|:-|
|<font color="red">A</font>|<font color="red">无名管道只允许具有亲缘关系的进程间通信，如父子进程间的通信。</font>|
|<font color="red">B</font>|<font color="red">管道只允许单向通信。</font>|
|<font color="red">C</font>|<font color="red">管道内部保证同步进制，从而保证访问数据的一致性。</font>|
|D|面向字节和结构数据均可。|
|<font color="red">E</font>|<font color="red">管道随进程，进程在管道在，进程消失管道对应的端口也关闭，两个进程都消失管道也消失。</font>|

