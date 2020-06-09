# 浙大城市学院课程资源共享计划
## 简介

**ZUCC INTERSECTION** 是一个提供一系列在浙江大学城市学院的生活、学习资源和信息的网站，我们是一个公益组织，不索取任何报酬。

我们在建的项目很多，你可以选择任何的一个项目进行维护。

### ZUCC课程补全计划
取名自EVA动画，是一个专注于提供课程资料和答案的项目，也是我们的主要维护项目。

### 美食禁书目录
同样取名自小说魔法禁书目录，里面的女主角index是个吃货，这个项目包括城院内部和周边的一系列美食资讯。

### PTA Solutions
还在为熬夜刷PTA烦恼吗，这个项目旨在维护PTA编程平台的所有编程题答案，希望ACM大佬们多多贡献。

---

我们使用mkdocs构建这个网站，mkdocs使用了python来构建它的项目，但是你不需要会任何python语法，因为所有的配置都以yaml的形式写在`mkdocs.yml`中，非常容易掌握。

并且你不需要改其他复杂的设置，唯一需要改的可能就是`nav`部分。

**这个仓库可能不会很快建成，我们的确非常需要你的帮助，请把你在日常生活和学习中搜集的资源发到我们的平台。**

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

#### 运行

```shell
mkdocs serve
```

然后在浏览器中输入地址: [http://localhost:8000/](http://localhost:8000/)

---

### docker快速运行指南

未来可能支持，目前正在做了，但是我课程太多了，暑假再说。

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

我们提供了一个脚本，叫做`build.py`。

运行这个脚本，就可以编译到 lifeinzucc.github.io 的网站上了。
