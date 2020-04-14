### 1.下列关于VLAN的说法中哪项正确?
|编号|选项|
|:-|:-|
|A|可删除或重命名VLAN 1。|
|B|Catalyst交换机最多可支持255个VLAN。|
|<font color="red">C|<font color="red">交换机在VLAN 1中使用CDP通告来检测相邻设备信息。|
|D|扩展VLAN允许同时向单个端口分配多个VLAN。|

### 2.网络管理员正在从交换机删除多个VLAN。当管理 员输入no vlan1命令时，收到错误消息。此命令为什么产生错误消息?
|编号|选项|
|:-|:-|
|A|VLAN只能由创建它的用户来删除。|
|B|只有将VLAN 1的角色分配给其它VLAN后，才能删除VLAN1。|
|C|只有删除VLAN 1的所有端口后才能删除VLAN 1。|
|<font color="red">D|<font color="red">VLAN 1是默认的管理VLAN,无法将其删除。|

### 3.Switch-A和Switch-B均配置有分别处于营销部、销售部、会计部和行政部VLAN中的端口。每个VLAN包含12名用户。需要多少个子网才能在所有VLAN之间实现路由连通?
|编号|选项|
|:-|:-|
|A|1|
|<font color="red">B|<font color="red">4|
|C|12|
|D|48|

### 4.默认情况下，中继链路属于哪个VLAN?
|编号|选项|
|:-|:-|
|A|所定义的第一个VLAN|
|B|所定义的最后一个VLAN|
|<font color="red">C|<font color="red">所有的VLAN|
|D|编号最小的VLAN|

### 5.网络管理员必须怎样做才能将快速以太网端口fa0/1从VLAN 2中删除并将其分配给VLAN 3?
|编号|选项|
|:-|:-|
|A|在全局配置模式下输入 no vlan 2和vlan3 命令。|
|B|在接口配置 模式下输入noswitchport access vlan 2命令，然后将该端口分配给VLAN 3。|
|<font color="red">C|<font color="red">在接口配置模式下输入switchport access vlan3命令。|
|D|关闭该接口以将其恢复到默认配置，然后将其分配给VLAN 3。|

### 6.以下哪项不属于默认交换机配置中的VL AN1的特点?
|编号|选项|
|:-|:-|
|A|CDP消息只会在VLAN1中发送。|
|B|VLAN1被保留供交换机之间的链路使用。|
|C|所有交换机端口都是VLAN1的成员。|
|<font color="red">D|<font color="red">仅交换机端口0/1被分配给VLAN1。|

### 7.下列哪种说法正确描述了VLAN的优点?
|编号|选项|
|:-|:-|
|A|VLAN通过调节流量控制和窗口大小来提升网络性能。|
|B|VLAN使交换机可通过VLAN ID过滤将数据包路由到远程网络。|
|C|VLAN通过减少交换机上所需的物理端口数量来降低网络开销。|
|<font color="red">D|<font color="red">VLAN将网络划分为较小的逻辑网络，这降低了网络对广播风暴的敏感性。|

### 8.在处于不同的VLAN中的设备间配置通信需要使用OSI模型中的哪个层?
|编号|选项|
|:-|:-|
|A|第1层|
|<font color="red">B|<font color="red">第3层|
|C|第4层|
|D|第5层|

### 9.应该在交换机上采用什么端口分配模式，才能连接来自语音和数据VLAN的流量?
|编号|选项|
|:-|:-|
|<font color="red">A|<font color="red">静态VLAN端口成员，但需要在端口上启用所有VLAN|
|B|静态VLAN端口成员，但需要在端口上启用语音和数据VLAN|
|C|语音VLAN端口成员，它可为这两种VLAN提供连接|
|D|动态VLAN端口成员，它会动态交换来自语音和数据VLAN的流量|

### 10.交换机端口fa0/1被手动配置为中继端口，现在拟用于将一台主机连接到网络。 网络管理员应该怎样重新配交换机端口fa0/1?
|编号|选项|
|:-|:-|
|A|在全局配置模式 下删除该端口上的多个VLAN。|
|B|在接口配置模式下输入switchport nonegotiate命令。|
|C|关闭该接口，然后重新启用，使其恢复默认配置。|
|<font color="red">D|<font color="red">在接口配置模式下输入switchport mode access命令。|

### 11.当删除VLAN时，该VLAN的成员端口会发生什么变化?
|编号|选项|
|:-|:-|
|A|它们会默认返回到管理 VLAN中。|
|B|它们会自动成为VLAN1的成员。|
|C|必须将它们分配给其它VLAN,才能删除原始VLAN.|
|<font color="red">D|<font color="red">它们仍然保持该VLAN的成员身份。直到交换机重新启动后，它们将成为管理VLAN的成员。|

### 12.帧标记会向每个帧中添加什么信息，以使帧可以通过交换中继线传输?
|编号|选项|
|:-|:-|
|A|目的MAC地址|
|B|交换机的MAC地址|
|<font color="red">C|<font color="red">VLAN ID|
|D|BID|

### 13.网络管理员希望将大楼A中的主机划分到编号分别为20和30的VLAN中，下列关于VLAN配的说法中哪项正确?
|编号|选项|
|:-|:-|
|A|VLAN 信息保存在启动配置中。|
|<font color="red">C|<font color="red">网络管理员可在全局配置模式或VLAN数据库模式下创建VLAN。|
|D|两个 VLAN都可命名为BUILDING A以与处于不同地理位置的其它VLAN区分。|

