## 拥有管理员权限的贡献者

克隆项目到本地

```
git clone https://github.com/lifeInZUCC/ZUCC-intersection --depth=1
```

创建develop分支。

```
git branch develop
```

切换到develop分支开发。

```
git checkout develop
```

向分支提交代码。

```
git add -A
git commit -m "update xxx"
```

切换和合并develop分支到master分支。

```
git checkout master
git merge develop
```

更新到远程仓库。

```
git push origin master
```

删除develop分支。

```
git branch -d develop
```

## 其他贡献者
到[github仓库地址](https://github.com/lifeInZUCC/ZUCC-intersection)，点击fork到自己的仓库中。

克隆自己的仓库

```
git clone https://github.com/你的github账号/ZUCC-intersection --depth=1
```

提交更改的代码。

```
git add -A
git commit -m "update xxx"
```

更新到远程仓库。

```
git push origin master
```

在github上给原始仓库提交合并请求。

[官方教程](https://help.github.com/assets/images/help/repository/repo-tabs-pull-requests.png)

等待管理员同意。