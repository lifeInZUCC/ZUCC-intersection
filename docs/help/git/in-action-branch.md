# Git实战（分支篇）

## 基本操作

### 创建分支

```
git branch develop
```

这个命令会创建一个名叫 `develop` 的分支。

### 切换分支

```
git checkout develop
```

这个命令会切换分支到 develop 分支，前提是你之前已经创建过了。

这个命令的本质其实就是移动了 `HEAD` 指针。

默认状态下，使用的是 master 分支。

### 创建并切换

```
git branch -b develop
```

结合了上面两个步骤。

### 合并分支

我们先切换回 master 分支。

```
git checkout master
```

现在把 develop 分支合并到 master 分支。

```
git merge develop
```

## 我们的网站推荐的开发方法

针对两类不同的贡献者。

### 加入我们团队的贡献者

我们提供参考的一个模版:

```
git clone https://github.com/lifeInZUCC/ZUCC-intersection --depth=1
git branch develop
git checkout develop
git add -A
git commit -m "update xxx"
git checkout master
git merge develop
```

### 其他贡献者

首先，你应该去 fork 到自己的仓库下。

![在这里插入图片描述](https://img-blog.csdnimg.cn/20200626032656933.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzMzMzg0NDAy,size_16,color_FFFFFF,t_70)

本地修改的模版:

```
git clone https://github.com/你的github账号/ZUCC-intersection --depth=1
git add -A
git commit -m "update xxx"
git push origin master
```

回到 Github，创建一个 Pull Request。

![在这里插入图片描述](https://img-blog.csdnimg.cn/20200626032921269.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzMzMzg0NDAy,size_16,color_FFFFFF,t_70)

等待我们的管理员同意。