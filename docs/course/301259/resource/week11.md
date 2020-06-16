### 1.消息数据元素(mtext)这个字段不但可以存储字符,还可以存储任何其他的数据类型型。
|编号|选项|
|:-|:-|
|<font color="red">A</font>|<font color="red">对</font>|
|B|错|

### 2.消息队列是采用链表数据结构实现的, writer 进程在链尾输入数据, read 进程在链首读出数据。因此它只支持单向通信。
|编号|选项|
|:-|:-|
|A|对|
|<font color="red">B</font>|<font color="red">错</font>|

### 3.不同于共享内存,内核完成向消息队列中发送消息后,会唤醒等待消息的进程。
|编号|选项|
|:-|:-|
|<font color="red">A</font>|<font color="red">对</font>|
|B|错|

### 4.在 ipc.h 中设置了一条消息的最大长度限制,和一个队列的最大长度限制。
|编号|选项|
|:-|:-|
|A|对|
|<font color="red">B</font>|<font color="red">错</font>|

### 5.消息队列的数据结构 msgid_ds 中登记了消息的最后发送进程的PID,和最后接收进程的PID。
|编号|选项|
|:-|:-|
|A|对|
|<font color="red">B</font>|<font color="red">错</font>|
