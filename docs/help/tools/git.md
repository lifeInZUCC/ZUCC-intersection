必须使用 git。

安装 git 可以到清华镜像站，因为官方的太慢了，目前只有 windows 版本的，[清华镜像站](https://mirrors.tuna.tsinghua.edu.cn/github-release/git-for-windows/git/Git%20for%20Windows%202.27.0/)。

其他系统使用一般包管理器就可以快速安装，比 windows 方便很多，可以参考[使用包管理器](./package-manager.md)。

对于不同权限的贡献者，你们使用的方式可能不太一样。

## 拥有管理员权限的贡献者

管理员权限，只要进了我们在 github 上的工作小组的人都自动拥有这个权限。

但是我们也在考虑是否要向所有人开放，因为人多了可能造成提交冲突。

**克隆项目到本地**

```
git clone https://github.com/lifeInZUCC/ZUCC-intersection --depth=1
```

--depth=1 代表只克隆最新的一条记录，可以缩小克隆的体积，但是意味着你不能版本回滚，因为本地没有以前的记录，所以，也可以选择性地去掉这个参数。

**本地创建 develop 分支。**

克隆下来的代码默认是 master 分支，但是考虑到提交冲突，直接在 master 分支上修改可能不是一个好的方案。所以我们建议使用双分支结构开发，但是对于一些不熟悉 git 的初学者来说，可能有些困惑。

事实上，git 的开发结构还有更加复杂的。这里不多说了。

对于双分支开发有兴趣的可以看一下下面的分析，但是使用 master 的单分支开发也行，到时候遇到提交冲突了，请找 2832203391@qq.com。

创建 develop 分支。

```
git branch develop
```

切换到 develop 分支开发。

```
git checkout develop
```

---

**向分支提交代码。**

无论是单分支结构还是双分支结构接下来的操作都一样。

当你修改了一个文件之后，就需要更新到分支里面去，add 命令把更新的文件放到一个提交的缓存里面，然后使用 commit 提交到分支里面去。

```
git add -A
git commit -m "update xxx"
```

commit 的-m 参数可以说明一些你更新或者修改了什么，不如 `update xxx`，`delete xxx`，`create xxx`。随你怎么写。

---

接下来是双分支结构的需要做的。

切换和合并 develop 分支到 master 分支。

```
git checkout master
git merge develop
```

---

接下来又是单双分支一样的操作。

上面只是在本地更新，如果你觉得本地更新得差不多了，想要提交到远程仓库，也就是我们在 github 的仓库，就需要以下操作。

**更新到远程仓库。**

```
git push origin master
```

删除 develop 分支。

```
git branch -d develop
```

## 其他贡献者

和上面差不多，但是你们是先把 fork 到自己的仓库，然后在自己的远程提交到自己的仓库，最后再把自己在 github 上的仓库合并到我们的名下，等待管理员同意。

**到[github 仓库地址](https://github.com/lifeInZUCC/ZUCC-intersection)，点击 fork 到自己的仓库中。**

**克隆自己的仓库**

```
git clone https://github.com/你的github账号/ZUCC-intersection --depth=1
```

**提交更改的代码。**

```
git add -A
git commit -m "update xxx"
```

**更新到远程仓库。**

```
git push origin master
```

**在 github 上给原始仓库提交合并请求。**

[官方教程](https://help.github.com/assets/images/help/repository/repo-tabs-pull-requests.png)

等待管理员同意。
