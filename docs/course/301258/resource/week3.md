## 进程概念

### 1.操作系统是通过( )对进程进行管理的。
|编号|选项|
|:-|:-|
|<font color="red">A</font>|<font color="red">进程控制块</font>|
|B|进程调度程序|
|C|临界区|
|D|进程启动程序|

### 2.进程并发执行的相对速度不能由进程自己来控制。
|编号|选项|
|:-|:-|
|<font color="red">A</font>|<font color="red">对</font>|
|B|错|

### 3.多道程序设计是指___。
|编号|选项|
|:-|:-|
|A|在实时系统中并发运行多个程序；|
|B|在分布系统中同一时刻运行多个程序；|
|C|在一台处理机上同一时刻运行多个程序；|
|<font color="red">D</font>|<font color="red">在一台处理机上并发运行多个程序；</font>|

### 4.多道程序环境下，操作系统分配资源以__为基本单位。
|编号|选项|
|:-|:-|
|A|程序|
|B|指令|
|<font color="red">C</font>|<font color="red">进程</font>|
|D|线程|

### 5.下面对进程的描述中，错误的是( )。
|编号|选项|
|:-|:-|
|A|进程是动态的概念|
|B|进程有生命期|
|<font color="red">C</font>|<font color="red">进程是指令的集合</font>|
|D|进程可以并发执行|


## 进程状态

### 1.进程具有三种基本状态：阻塞态、运行态、就绪态，进程在执行过程中，其状态总是在不停地发生变化的，下面关于进程状态变化的说法中正确的是( )。
|编号|选项|
|:-|:-|
|A|进程一旦形成，首先进入的是运行状态|
|B|三种进程状态是进程运行过程中的基本状态，进程可能同时处于某几种状态中|
|<font color="red">C</font>|<font color="red">在分时系统中，一个正在运行进程的时间片到，该进程将转入就绪状态</font>|
|D|一个进程必须经过进程的三个基本状态才能结束|

### 2.一个进程被唤醒意味着( )。
|编号|选项|
|:-|:-|
|A|该进程的优先数变为最大|
|B|该进程获得了CPU|
|<font color="red">C</font>|<font color="red">该进程从阻塞状态变为就绪状态</font>|
|D|该进程排在了绪队列的队首|

### 3.任一时刻，若有执行状态的进程，就一定有就绪状态的进程。
|编号|选项|
|:-|:-|
|A|对|
|<font color="red">B</font>|<font color="red">错</font>|

### 4.下列进程状态变化中，___变化是不可能发生的。
|编号|选项|
|:-|:-|
|A|运行一>就绪|
|B|运行一>等待|
|<font color="red">C</font>|<font color="red">等待一>运行</font>|
|D|等待一>就绪|

### 5.进程管理中，当___，进程从阻塞态变成就绪态。
|编号|选项|
|:-|:-|
|A|进程被进程调度程序选中|
|B|等待一个事件|
|<font color="red">C</font>|<font color="red">等待的事件发生</font>|
|D|时间片用完|

### 6.进程分配到必要的资源并获得处理机时的状态是( )。
|编号|选项|
|:-|:-|
|<font color="red">A</font>|<font color="red">运行状态</font>|
|B|就绪状态|
|C|阻塞状态|
|D|中断状态|


## 进程控制

### 1.操作系统通过切换进程标识符来进行进程切换。
|编号|选项|
|:-|:-|
|A|对|
|<font color="red">B</font>|<font color="red">错</font>|

### 2.( )必定会引起进程切换。
|编号|选项|
|:-|:-|
|<font color="red">A</font>|<font color="red">一个进程从运行态变成等待态</font>|
|<font color="red">B</font>|<font color="red">一个进程从运行态变成就绪态</font>|
|C|一个进程从等待态变成就绪态|
|<font color="red">D</font>|<font color="red">一个进程从就绪态变成运行态</font>|
|E|一个进程被创建后进入就绪态|

### 3.下列哪些指令必须是特权指令（也即只能在内核模式下运行）？
|编号|选项|
|:-|:-|
|<font color="red">A</font>|<font color="red">设置内核模式</font>|
|<font color="red">B</font>|<font color="red">系统重启动</font>|
|<font color="red">C</font>|<font color="red">读取程序状态字</font>|
|<font color="red">D</font>|<font color="red">关闭中断</font>|
|<font color="red">E</font>|<font color="red">写指令寄存器</font>|

### 4.用户可通过( )建立和撤销进程。
|编号|选项|
|:-|:-|
|A|函数调用|
|B|宏指令|
|<font color="red">C</font>|<font color="red">系统调用</font>|
|D|过程调用|

### 5.通常用户进程被建立后，( )。
|编号|选项|
|:-|:-|
|A|便一直存在于系统中，直到被操作人员撤消|
|<font color="red">B</font>|<font color="red">随着进程运行的正常或不正常结束而撤消</font>|
|C|随着时间片轮转而撤消与建立|
|D|随着进程的阻塞或唤醒而撤消与建立|

