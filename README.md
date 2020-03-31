## 项目安装指南
我们提供两种快速安装运行的方案：
- pip
- docker

### 使用pip搭建环境

#### 搭建python环境
首先要**确定的python能够正常工作**。

如果没问题那么就：

```shell
pip install -r requirements.txt
```

或者也许在你的机器上是：
```shell
pip3 install -r requirements.txt
```

#### 运行

```shell
mkdocs serve
```

---

### 使用docker获得环境

#### 拷贝docker镜像

```shell
docker pull squidfunk/mkdocs-material
```

#### 在docker中运行

```shell
docker run --rm -it -p 8000:8000 -v ${PWD}:/docs
```

在windows上是这样：

```powershell
docker run --rm -it -p 8000:8000 -v %cd%:/docs
```

---

## 编译部署

```shell
mkdocs build
```