## 关于文本编辑器的选择

### VSCode

作为一位深度 VSCode 用户，我强烈推荐把 VSCode 作为电脑上所有文本的编辑器。

[vscode 下载链接](https://code.visualstudio.com/)

就本项目的编辑而言，推荐的插件有:

-   两款美化插件`One Dark Pro`+`Material Icon Theme`。
-   一款 Markdown 扩展`Markdown All in One`，支持一些语法。
-   一款 Markdown 格式化工具，准确来说是基本支持所有语言了，叫`Pretter`。
-   项目管理插件`Project Manager`。把自己的项目保存在这里，下次打开编辑器就可以直接找到了。

关于 vscode 的 markdown 编辑工作，我给一个我自己的配置。

```json
/* 全局配置 */
"files.autoSave": "afterDelay",
"editor.formatOnPaste": true,
/* 仅Markdown类型的文件配置 */
"[markdown]": {
    "editor.wordWrap": "on",
    "editor.quickSuggestions": false,
    "editor.formatOnSave": true,
    "editor.defaultFormatter": "esbenp.prettier-vscode",
},
```

把这些代码放到 `settings.json` 中。

打开`settings.json`的方法是:

1. 快捷键 command+shift+p(macos) 或者 ctrl+shift+p(windows linux)。
2. 搜索`Open Settings (JSON)`。

如果有想和我讨论 vscode 的配置和使用，联系邮箱: 2832203391@qq.com 。

### Typora

除去 vscode，typora 也是不错的 Markdown 编辑器。

[typora 下载链接](https://typora.io/)

## 关于开发包

一般我们都会选择一些包管理器来管理开发包，linux 用户自然不用我说，有非常方便的包管理器。

这里主要针对 windows 和 mac 用户。

windows下的包管理器，比较著名的有chocolaty。

## Oh My Zsh

一遍一遍地输入命令行可能会让你非常崩溃，所以，对于 Linux 和 MacOS 用户，强烈推荐使用 oh-my-zsh。

Windows 用户可以通过搭建 [WSL2+Windows Terminal](https://www.sitepoint.com/wsl2-windows-terminal/) 的方式补救一下。然后再安装 Oh My Zsh。

[Oh My Zsh 下载链接](https://ohmyz.sh/)

## Git Bash

我们的项目中有一些用于自动化的 bash 脚本，对于 windows 用户来说，使用 git bash 可能是一个比较好的选择。当然 WSL2+Windows Terminal 也是相当好的。

安装完 git 的官方安装包，一般都会自带 Git Bash。

## Chrome 浏览器

我们自己的一个工具`Exercises Manager`中包含一个 chrome 插件。所以最好是用 chrome 系的浏览器。

## Python & pip

需要安装 python 解释器，一般都自带 pip。

## Node.js & npm

如果要使用`Exercises Manager`，需要安装 Node.js 解释器，一般都自带 npm 包管理器。
