## 线程

### 1.线程是调度的基本单位，但不是资源分配的基本单位。
| 选项||  
|--|--|
|<font color="#FF0000">A|<font color="#FF0000">F|
|B|T|

### 2.隶属于同一进程的多个线程共享一组CPU寄存器值，并共享一个堆栈。
|选项||
|--|--|
|A|T|
|<font color="#FF0000">B|<font color="#FF0000">F|

### 3.A thread is also called______.
|| 选项|  
|-|-|
A|a virtual process|
<font color="#FF0000">B|<font color="#FF0000">a lightweight process |
C|a heayweight process|
D|none of the above|

### 4.A Thread Control Blockstores(TCB)stores:
|| 选项|  
|-|-|
A|User (owner) ID|
B|Memory map|
<font color="#FF0000">C|<font color="#FF0000">The machine state(registers, program counter)|
D|Open file descriptors|

### 5.用户级线程不依赖于内核。
|选项||
|--|--|
|<font color="#FF0000">A|<font color="#FF0000">F|
|B|T|

## 进程并发

### 1.并发是指两个或多个事件( )。
|| 选项|  
|-|-|
A|在同一时刻发生|
<font color="#FF0000">B|<font color="#FF0000">在同一时间区段内发生|
C|两个进程相互交互|
D|在时间上相互无关|

### 2.单处理机上可以并发执行多个程序。
|选项||
|--|--|
|<font color="#FF0000">A|<font color="#FF0000">对|
|B|错|

### 3.以下()是程序并发执行的特点。
|| 选项|  
|-|-|
A|顺序性|
B|封闭性|
<font color="#FF0000">C|<font color="#FF0000">间断性|
D|可再现性|

### 4.顺序程序和并发程序的执行相比，( )。
|| 选项|  
|-|-|
A|完全相同|
<font color="#FF0000">B|<font color="#FF0000">并发程序执行总体上执行时间快|
C|运行结果都唯一|
D|顺序程序执行总体上执行时间快|

### 5. 进程并发执行时可能会产生与时间有关的错误。形成这种错误是由于若干进程( )
|选项||
|--|--|
<font color="#FF0000">A|<font color="#FF0000">交替地访问了共享变量|
B|改变了各自的执行顺序|
C|占用处理器的时间太长|
D|执行了相同的程序|

## 进程互斥

### 1.对临界资源，应采用互斥访问方式来实现共享。
|选项||
|--|--|
|<font color="#FF0000">A|<font color="#FF0000">对|
|B|错|

### 2.一次仅允许一个进程使用的资源叫临界资源，所以对临界资源是不能实现共享的。
|选项||
|--|--|
|A|对|
|<font color="#FF0000">B|<font color="#FF0000">错|

### 3.即便线程不作为资源分配单位，线程之间仍可能因为竞争影响并行执行。
|选项||
|--|--|
|<font color="#FF0000">A|<font color="#FF0000">对|
|B|错|

### 4.The cititcal section of a concurrent process is__.
|| 选项|  
|-|-|
A|a buffer|
B|a data section|
C|a synchronization mechanism|
<font color="#FF0000">D|<font color="#FF0000">a segment of code|

### 5.The citical resource for process synchronization is __.
|| 选项|  
|-|-|
A|a resource that cannot be recovered if the system fails|
<font color="#FF0000">B|<font color="#FF0000">a data section|
C|a snchonization mechanism|
D|a segment of code|