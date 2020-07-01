### 1.下列哪些函数或系统调用涉及发送信号：
|编号|选项|
|:-|:-|
|A|signal()|
|<font color="red">B</font>|<font color="red">alarm()</font>|
|<font color="red">C</font>|<font color="red">sigqueue()</font>|
|D|sigaction()|
|<font color="red">E</font>|<font color="red">raise()</font>|
|F|pause()|
|<font color="red">G</font>|<font color="red">kill()</font>|

### 2.例程8，正确的运行方式是：
|编号|选项|
|:-|:-|
|A|发送进程先运行./ss，接收进程后运行./rr|
|<font color="red">B</font>|<font color="red">接收进程先运行./rr signum，发送进程后运行./ss signum pid</font>|
|C|发送进程先运行./ss signum pid，接收进程后运行./rr signum|
|D|接收进程先运行./rr signum pid，发送进程后运行./ss signum|

