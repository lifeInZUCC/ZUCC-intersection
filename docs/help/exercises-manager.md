Exercises Manager是一个用于抓取网页中的习题，制作成Markdown格式，在博客分享的工具链。

由`ZUCC INTERSECTION`的管理员之一[nonlinearthink](https://github.com/nonlinearthink)维护，历史比`ZUCC INTERSECTION`还要久。

这个项目基于 Node.js ，包括以下内容:
- 一个chrome浏览器插件，用于从网页上爬取题目。
- 一个本地的命令行工具，用于处理题目文件。

## 安装说明

1. 下载[Node.js](https://nodejs.org/zh-cn/download/)，注意安装的时候同时安装npm。
2. 克隆仓库到本地:
    ```
    git clone https://github.com/nonlinearthink/exercises-manager --depth=1
    ```
3. 到本地的项目根目录下，运行`npm install`安装项目依赖。

## 使用说明

## chrome插件

在浏览器中打开链接[chrome://extensions/](chrome://extensions/)。

找到右上角的一个开关，开启开发者模式。

在左上角找到加载插件，选择刚刚克隆的项目中的一个chrome子文件夹，选中它导入。

## 命令行快速入门

