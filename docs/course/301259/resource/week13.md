### 1.字符设备和块设备的驱动设计有很大差异，但对于用户而言，它们都要使用文件系统的操作接口，如open(),close(),read()，write()等进行访问。
|编号|选项|
|:-|:-|
|<font color="red">A</font>|<font color="red">对</font>|
|B|错|

### 2.每个模块由目标代码组成（没有连接成一个完整可执行文件），可以通过insmod程序动态连接到运行中的内核中，以及通过rmmod程序去除连接。
|编号|选项|
|:-|:-|
|<font color="red">A</font>|<font color="red">对</font>|
|B|错|

### 3.Linux把外部设备划分为字符设备、块设备和网络设备。其中，__属于块设备。
|编号|选项|
|:-|:-|
|A|串行口|
|B|图形终端|
|<font color="red">C</font>|<font color="red">IDE硬盘</font>|
|D|打印机|

### 4.__设备是字符设备。
|编号|选项|
|:-|:-|
|A|/dev/hdc|
|B|/dev/sda|
|C|/dev/hda1|
|<font color="red">D</font>|<font color="red">/dev/tty1</font>|