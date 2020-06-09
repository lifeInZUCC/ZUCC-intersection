mkdocs 这个框架是 python 写的，但是你不需要了解 python。只要会跑我们的这个项目就行了。

## 关于项目的安装和使用

在根目录下面使用 pip 安装所有的环境。

```
pip install -r requirements.txt
```

之后就可以运行了，使用 mkdocs 的 server 命令可以边修改边看网页的变化。

```
mkdocs server
```

这之后应该会跳出一个地址，一般是 http://127.0.0.1:8000，浏览器打开这个地址就可以在本地预览网页了。

## 关于项目的编译和部署到 github.io 上去

根目录下面有一个简单的脚本，叫做 build.py，只要运行就行了。

记得用 python3.x 版本运行。linux 和 mac 的用户注意了，一般你们的安装的 python3.x 在命令行中的运行命令都不是 python，而是 python3，同样，pip 应该使用 pip3。
