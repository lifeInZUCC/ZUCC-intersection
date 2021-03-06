## 知识回顾

### 1.在分页时，每个进程拥有一个页表，且页表驻留在内存中。
|编号|选项|
|:-|:-|
|<font color="red">A|<font color="red">对|
|B|错|

### 2.页式存储管理中，一个作业可以占用不连续的内存空间，而段式存储管理，一个作业则是占用连续的内存空间。
|编号|选项|
|:-|:-|
|A|对|
|<font color="red">B|<font color="red">错|

### 3.下列选项中对分段存储管理叙述正确的是()。
|编号|选项|
|:-|:-|
|A|分段存储管理中每个段必须是大小相等的|
|<font color="red">B|<font color="red">每一段必须是连续的存储区|
|C|每一段不必是连续的存储区|
|D|段间的存储区必须是连续的|

### 4.A system with 32-bit addresses 1GB main memory, and a 1 megabyte(20-bit) page size will have a page table that contains () entries.
|编号|选项|
|:-|:-|
|<font color="red">A|<font color="red">4K|
|B|4M|
|C|1M|
|D|1K|

### 5.In a system using segmentation, the logical address is expressed in 32 bits within which 20 bits are used as segment number. The maximum size of each sehment is_.
|编号|选项|
|:-|:-|
|<font color="red">A|<font color="red">2^12|
|B|2^16|
|C|2^20|
|D|2^32|

### 6.虚拟存储管理系统的基础是程序的()理论。
|编号|选项|
|:-|:-|
|A|动态性|
|B|全局性|
|<font color="red">C|<font color="red">局部性|
|D|虚拟性|

### 7.()是请求分页存储管理方式和基本分页存储管理方式的区别。
|编号|选项|
|:-|:-|
|A|不必将作业装入连续区域|
|B|地址重定向|
|C|采用快表技术|
|<font color="red">D|<font color="red">不必将作业全部装入内存|

### 8.引入TLB（快表）是为了解决分页时两次内存访问的问题。
|编号|选项|
|:-|:-|
|<font color="red">A|<font color="red">对|
|B|错|

### 9.在请求分页式系统中，以页为单位管理用户的虚空间，以段为单位管理内存空间。
|编号|选项|
|:-|:-|
|A|对|
|<font color="red">B|<font color="red">错|

### 10.Consider a demand-paging system with the following time-measured utilizations:

```
CPU utilization 20%
Paging disk 97.7%
Other I/O devices 5%
```

Which (if any) of the following will (probably) improve CPU utilization?

|编号|选项|
|:-|:-|
|A|to install a faster hard disk|
|B|to increase swap space with large capacity hard disk|
|C|to increase the number of running processes|
|<font color="red">D|<font color="red">to increase physical memory capacity via increasing memory chips|

## 缺页中断和页面替换

### 1.虚拟存储器的最大容量（）。
|编号|选项|
|:-|:-|
|A|由作业的地址空间决定|
|B|是任意的|
|<font color="red">C|<font color="red">由计算机的地址结构决定的|
|D|为内、外容量之和|

### 2.进程在执行中发生了缺页中断，经操作系统处理后，应让其执行（）指令。
|编号|选项|
|:-|:-|
|<font color="red">A|<font color="red">被中断的那一条|
|B|被中断的后一条|
|C|启动时的那一条|
|D|被中断的前一条|

### 3.考虑页面置换算法，系统有m个物理块供调度，初始时全空，页面引用串长度为p，包含了n个不同的页号，无论用什么算法，缺页次数不会少于（）。
|编号|选项|
|:-|:-|
|A|min(m, n)|
|<font color="red">B|<font color="red">n|
|C|m|
|D|p|

### 4.In a demanding paging system, the size of a page is 4KB. A process access the logical address 12345(0x3039)will ___ if the page table is as the following:

```
Page#  Frame#  Vaildity
0      3       v
1      4       v
2      2       v
3      -       i
```

|编号|选项|
|:-|:-|
|A|access physical address 4*4096+57|
|B|access physical address 3*4096+57|
|C|access physical address 2*4096+57|
|<font color="red">D|<font color="red">cause a page-fault interrupt|

### 5.在请求分页系统中，若逻辑地址中的页号超过页表寄存器中的页表长度，则会引起（）。
|编号|选项|
|:-|:-|
|A|输入输出中断|
|B|时钟中断|
|<font color="red">C|<font color="red">越界中断|
|D|缺页中断|

### 6.With the demanding paging,__has best system performance.
|编号|选项|
|:-|:-|
|<font color="red">A|<font color="red">stacks|
|B|lists|
|C|hashed tables|
|D|arrays|

