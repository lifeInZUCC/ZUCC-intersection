### 1.A process may use the system call signal() to change the handler function of a selected signal number, except SIGKILL(9) and SIGSTOP(19). 进程通过系统调用signal来指定进程对某个信号的处 理行为，但SIGKILL，SIGSTOP这两个信号不可被改变。
|编号|选项|
|:-|:-|
|<font color="red">A</font>|<font color="red">对</font>|
|B|错|

### 2.What is the result of the command:kill -9 13459
|编号|选项|
|:-|:-|
|<font color="red">A</font>|<font color="red">Kill PID 13459 with a signal 9</font>|
|B|Kill PID 13459 with a signal 15|
|C|Kill PID 13459 with a signal 1|
|D|None of the above|

### 3.Linux的文件类型众多，基至包含一些特殊文件。但是，__不属于Linux的文件。
|编号|选项|
|:-|:-|
|A|pipe|
|B|第一块硬盘的逻辑名|
|<font color="red">C</font>|<font color="red">signal</font>|
|D|shell命令"zcat thread.c.gz | grep main -"中的符号"|"|

### 4.When the kill command is given with only the PID number of the process to kill (as in "kill 1234") , this corresponds to which type of kill signal?
|编号|选项|
|:-|:-|
|A|2(SIGINT)|
|B|1(SIGHUP)|
|G|9(SIGKILL)|
|<font color="red">D</font>|<font color="red">15(SIGTERM)</font>|

### 5.收到信号的进程对各种信号有不同的处理方法。处理方法可以分为三类：第一种是类似中断的处理程序，对于需要处理的信号，进程可以指定处理函数，由该函数来处理： 第二种方法是，忽略某个信号，对该信号不做任何处理，就像未发生过一样; 第三种方法是，对该信号的处理保留系统的默认值。 进程通过系统调用( ) 来指定进程对某个信号的处理行为。
|编号|选项|
|:-|:-|
|A|kill|
|<font color="red">B</font>|<font color="red">signal</font>|
|<font color="red">C</font>|<font color="red">sigaction</font>|
|D|alarm|
|E|sigqueue|

