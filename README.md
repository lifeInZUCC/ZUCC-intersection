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

## 入门指南

### python/pip 环境安装

根据自己的操作系统安装 python/pip 环境。

macOS 和 Linux，一般默认 python命令行 是链接到 python2.x 上去的，对于这两个操作系统来说，以下所有的操作都要换成 python3/pip3。

安装 mkdocs 运行依赖

```shell
pip install -r requirements.txt
```

> 其中包括一个 mkdocs 的命令行程序。接下来你可以使用 mkdocs 命令行了。

### 运行

```shell
mkdocs serve
```

然后在浏览器中输入地址: [http://localhost:8000/](http://localhost:8000/)

### 更改/添加内容

##### 学习markdown

首先，你需要会markdown，非常容易，网上教程翻一眼就好了。

除了用了标准的markdown格式，我们还自己用了一些非常酷炫的扩展语法，我们认为可以有效提高文档的观感，所以配置了一下。具体可以看我们网站上的[教程](https://lifeinzucc.github.io/example/admonition/)。

##### 编写markdown和添加界面

在项目的`docs`及其子目录下面创建`.md`结尾的文件。

目前没办法做到自动化，我们需要到`mkdocs.yml`文件中，找到一个`nav`那一栏。

```yaml
# Page tree
nav:
  - 简介: index.md
  - 我们的故事: log.md
  - 关于我们的组织: about.md
  - ZUCC课程补全计划:
      - 简介: course/Readme.md
```

以`docs`为根目录，把相对地址写到 nav 的配置里面，冒号前面的是界面的名称，后面是地址。

理论上来讲目录结构是多级的，可以无限扩展下去，但是我们也没做过测试。

### 项目编译部署指南

我们提供了一个脚本，叫做`build.py`。

运行这个脚本，就可以编译到 lifeinzucc.github.io 的网站上了。
