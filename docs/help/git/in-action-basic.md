# Git实战（基础篇）

## 获得一个 Git 项目

### 初始化项目

在当前目录下，使用命令:

```shell
git init
```

会创建一个 `.git` 的文件夹，现在，这个目录就被转换成 Git 项目。

### 克隆

还有一个获得一个 Git 仓库的办法，就是克隆别人的仓库。

```shell
git clone https://github.com/lifeInZUCC/ZUCC-intersection
```

这会在当前目录创建一个名叫 `ZUCC-intersection` 的文件，然后从后面的链接位置把整个仓库克隆下来，这就是我们所说的分布式的概念。

一般情况下，Github 不太容易出现数据丢失，所以我一般还习惯另外一个操作:

```shell
git clone https://github.com/lifeInZUCC/ZUCC-intersection --depth=1
```

`--depth=1` 代表只克隆最近的一个记录，可以节省很多存储空间和克隆时间，特别对于迭代周期比较长和比较大的项目来说。

## 文件状态转换

### 暂存文件

使用`git add`命令可以把文件加入 Git 的追踪系统，也就是变成`staged`状态。

当我们修改了这个文件之后，它就变成`modified`状态。

需要再次使用`git add`命令，文件才会再次变成`staged`状态。

Git 的文件通配符就是 shell 的通配符，对 shell 脚本熟悉的话就懂了。

```shell
git add *
```

这条命令会把文件夹下所有文件都加入 Git 的追踪。

有一个例外就是，编写`.gitignore`，可以忽略一些文件，永远不会被 Git 追踪，可以自己去查怎么编写。

值得一提的是，这种情况下使用`git add *`会出现警告，我一般推荐使用`git add -A`，都是添加全部文件，但是它会先检查`.gitignore`里的内容。

### 提交代码

`git commit` 命令会把`staged`状态的文件转为`commited`状态。也就是提交到当前的分支中去。

```shell
git commit -m "update xxx"
```

`-m` 参数后加一个字符串，可以为提交代码做一些说明。

## 远程仓库相关

### 添加远程仓库

如果你是通过克隆创建的 Git 项目，那么这条对你没什么意义。克隆的项目，这一项已经默认配好了，当然，如果你想要同步到多个平台，当我没说。

自己创建的项目要发布到 `Github` 上，就要添加一个远程仓库。比如:

```
git remote add origin git@github.com:nonlinearthink/ZUCC-intersection
```

这句话的意思是设置了一个默认的远程仓库，名叫 `origin`。

### 发布到远程仓库

使用 `git push` 命令实现。

```
git push origin master
```

这代表把当前分支发布到 origin 远程仓库的 master 分支上。

### 同步远程仓库

在多人合作的场景下，如果别人改了远程仓库，我们就需要把别人的更改的内容同步到本地。

```
git fetch
```

`fetch` 只检查远程仓库和本地仓库的内容，但不更新。

```shell
git pull
```

`pull` 会直接更新。
