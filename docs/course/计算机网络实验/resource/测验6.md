### 1.下列哪一个地址可以用来总结网络 172.16.1.0/24 、 172.16.2.0/24 、 172.16.3.0/24 和 172.16.4.0/24 ？
|编号|选项|
|:-|:-|
|<font color="red">A|<font color="red">172.16.0.0/21|
|B|172.16.1.0/22|
|C|172.16.0.0 255.255.255.248|
|D|172.16.0.0 255.255.252.0|

### 2.两个独立子网上的主机之间无法通信。网络管理员怀疑其中一个路由表中缺少路由。不能使用哪条命令来帮助排查第 3 层连通性问题？
|编号|选项|
|:-|:-|
|A|ping|
|<font color="red">B|<font color="red">show arp|
|C|traceroute|
|D|show ip route|

### 3.当外发接口不可用时，路由表中的静态路由条目有何变化？
|编号|选项|
|:-|:-|
|<font color="red">A|<font color="red">该路由将从路由表中删除。|
|B|路由器将轮询邻居以查找替用路由。|
|C|该路由将保持在路由表中，因为它是静态路由。|
|D|路由器将重定向该静态路由，以补偿下一跳设备的缺失。|

### 4.Router# show interfaces serial 0/1 命令的输出显示了如下内容：Serial0/1 is up, line protocol is down.线路协议为 down （关闭）的原因最可能是什么？
|编号|选项|
|:-|:-|
|A|Serial0/1 为关闭状态。|
|B|路由器未连接电缆。|
|C|远程路由器正在使用 serial 0/0 接口。|
|<font color="red">D|<font color="red">尚未设置时钟频率。|

### 5.为什么需要在创建输出接口为以太网络的静态路由时输入下一跳 IP 地址？
|编号|选项|
|:-|:-|
|A|添加下一跳地址将使路由器在转发数据包时不再需要在路由表中进行任何查找。|
|<font color="red">B|<font color="red">在多路访问网络中，如果没有下一跳地址，路由器将无法确定以太网帧的下一跳 MAC 地址。|
|C|在静态路由中使用下一跳地址可以为路由提供较低的度量。|
|D|在多路访问网络中，在静态路由中使用下一跳地址可以使该路由成为候选默认路由。|

### 6.网络服务出现故障时，通常使用哪个端口访问路由器进行管理？
|编号|选项|
|:-|:-|
|A|以太网|
|B|控制台|
|C|Telnet|
|<font color="red">D|<font color="red">SSH|

### 7.下列哪项不是路由器的功能？
|编号|选项|
|:-|:-|
|A|网段扩展|
|B|广播域分段|
|C|根据逻辑编址选择最佳路径|
|<font color="red">D|<font color="red">根据物理编址选择最佳路径|

### 8.路由器具有到达每个目的网络的静态路由。下列哪种情况需要管理员变更该路由器上配置的静态路由？
|编号|选项|
|:-|:-|
|A|目的网络移到同一路由器的不同接口。|
|B|源和目的地之间的路径已升级为带宽更高的链路。|
|<font color="red">C|<font color="red">拓扑结构发生变化，导致现有的下一跳地址或送出接口无法访问。|
|D|出于维护目的，远程目的网络接口需要关闭 15 分钟。|

### 9.网络管理员在 Router1 中输入了以下命令： ip route 192.168.0.0 255.255.255.0 S0/1/0 。 Router1 随后收到发往 192.168.0.22/24 的数据包。在路由表中找到最近刚配置的静态路由之后， Router1 接下来将如何处理该数据包？
|编号|选项|
|:-|:-|
|A|丢弃该数据包，因为路由表中未列出目的主机|
|B|查找 S0/1/0 接口的 MAC 地址以确定新帧的目的 MAC 地址|
|C|在转发该数据包之前递归查找 S0/1/0 接口的 IP 地址|
|<font color="red">D|<font color="red">将该数据包封装到适合该 WAN 链路的帧中，并将其从 S0/1/0 接口转发出去|

### 10.将默认的路由器名称更改为ZUCC使用哪条命令？
|编号|选项|
|:-|:-|
|A|Router# name ZUCC|
|B|Router# hostname ZUCC|
|C|Router(config)# name ZUCC|
|<font color="red">D|<font color="red">Router(config)# hostname ZUCC|

### 11.下列哪条命令可将路由器置于正确模式，用于配置适当的接口连接到 LAN ？
|编号|选项|
|:-|:-|
|A|UBAMA(config)# line vty 0 4|
|B|UBAMA(config)# line console 0|
|C|UBAMA(config)# interface Serial 0/0/0|
|<font color="red">D|<font color="red">UBAMA(config)# interface FastEthernet 0/1|

### 12.路由器完成启动步骤后，网络管理员希望立即检查路由器配置。管理员从特权执行模式可以使用以下哪个命令达到此目的？
|编号|选项|
|:-|:-|
|A|show flash|
|B|show NVRAM|
|<font color="red">C|<font color="red">show running-config|
|D|show version|

