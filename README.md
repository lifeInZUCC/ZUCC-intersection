# 浙大城市学院课程资源共享计划
## 简介

**浙大城市学院课程资源共享计划**是为了帮助 ZUCC 的学子们不再受课程的折磨，拥有更好的生活而发起的项目，我们的计划是建立一个提供 ZUCC 所有正在进行的课程的资源库。

这个资源库会包括以下的资源：

- 教材
- 课件
- 历年试题卷
- 题库
- 辅助资料

我们使用mkdocs构建这个网站，是模仿了其他的高校，在网上可以搜到类似的很多项目，mkdocs使用了python来构建它的项目，但是你不需要会任何python语法，因为所有的配置都以yaml的形式写在`mkdocs.yml`中，非常容易掌握。

并且你不需要改其他复杂的设置，唯一需要改的可能就是`nav`部分。我们下面会详细介绍怎么改，所以你也不需要担心。

这个仓库可能不会很快建成，所以要对那些已经发现了我们的项目并希望在上面找到一些资源的人说一声对不起。但同时，我们的确非常需要你的帮助，请把你在日常学习中搜集的资源发到我们的平台，帮助更多的人更好地学习。

最后，欢迎各位 ZUCC 的学子们为本仓库贡献课程资料。

## 项目安装指南
我们提供两种快速安装运行的方案：
- pip
- docker

### pip快速运行指南

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

然后在浏览器中输入地址: [http://localhost:8000/](http://localhost:8000/)

---

### docker快速运行指南

#### 拷贝docker镜像

```shell
docker pull squidfunk/mkdocs-material
```

#### 在docker中运行

##### linux/mac

```shell
docker run --rm -it -p 8000:8000 -v ${PWD}:/docs
```

##### windows

```powershell
docker run --rm -it -p 8000:8000 -v %cd%:/docs
```

最后在浏览器输入地址：[http://localhost:8000/](http://localhost:8000/)

---

## 更改/添加内容
### 学习markdown
首先，你需要会markdown，这是一种文件编辑的格式，它可以方便地给文档做一些标记，以形成一定的显示效果。

我们的项目除了用了标准的markdown格式，还用了一些非常酷炫的扩展语法，可以有效提高文档的质量。具体可以看我们网站上的[教程](https://lifeinzucc.github.io/example/admonition/)。

在项目的`docs`目录下面创建`.md`结尾的文件，然后编辑你要添加的文档，最后它会被编译成HTML。你可以对照一下我们的docs源代码和[网站](https://lifeinzucc.github.io)上显示的内容就会明白怎么回事。

### 添加页面到配置文件

对不起，我们暂时没有什么好方法来自动化这一过程，在完成上面的步骤之后，你也许会发现，似乎并没有新的页面添加到网页中。

事实上需要到`mkdocs.yml`文件中，找到一个`nav`那一栏，例如:

```yaml
nav:
    - 简介: index.md
    - 关于本项目: about.md
    - Markdown扩展语法:
          - "警告框语法": "example/admonition.md"
          - "代码块扩展语法": "example/codehilite.md"
          - "其他扩展语法": "example/others.md"
```

上面的代码的意思就是绑定导航栏和你的源文件，例如第一级是由三个界面`简介` `关于本项目` `Markdown扩展语法`三个部分组成的，冒号后面的内容是源文件，冒号前面的内容是最后显示的网页名称。

除了第一级目录还可以有第二级、第三级等等，可以有多级目录。

项目的首页是名为`index.md`的文件对应的网页，所以在这里首页就是`简介`页。

## 项目编译部署指南

上面的步骤之后，最后一步是要把项目编译并且提交到github上。

- 首先你需要一个github账号。

- 



```shell
mkdocs build
```