# exercises-manager

## 简介

用于制作个人在线习题，一套把题目转成 Markdown 格式的工具链。

基本工作模式:

-   使用 chrome 插件在特定的页面爬取题目，保存成 JSON 文件。
-   使用命令行工具处理 JSON 文件，转换成 Markdown 的格式。

目前支持的网页:

| 网站                                    | 题目类型               |
| --------------------------------------- | ---------------------- |
| [中国大学 MOOC](https://icourse163.org) | 单选、多选、判断、填空 |
| [BB 教学平台]()                         | 单选、判断             |
| [PTA](https://pintia.cn)                | 单选、判断             |

可以到[github issue](https://github.com/lifeInZUCC/Exercises-Manager/issues)提供你的建议。

## 安装说明

你可能需要了解一点 Node 和 npm 。

1. 下载[Node.js](https://nodejs.org/zh-cn/download/)，**注意同时安装 npm**。
2. 克隆 exercises-manager 到本地:
    ```
    git clone https://github.com/lifeInZUCC/Exercises-Manager --depth=1
    ```
3. 如果已经安装了 npm，运行`npm install`安装项目依赖。

## Chrome 插件使用

### 具体操作:

1. 在浏览器中打开[chrome://extensions/](chrome://extensions/)。
2. 开启开发者模式。

    ![extension.jpg](https://img-blog.csdnimg.cn/20200507010226219.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzMzMzg0NDAy,size_16,color_FFFFFF,t_70)

3. 选择刚刚克隆的项目中的一个 chrome 子文件夹，导入。

    ![select.jpg](https://img-blog.csdnimg.cn/20200507010242784.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzMzMzg0NDAy,size_16,color_FFFFFF,t_70)

4. 点击相应的按钮就可以抓取题库。

    ![popup.png](https://img-blog.csdnimg.cn/20200507010302305.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzMzMzg0NDAy,size_16,color_FFFFFF,t_70)

## 命令行使用

使用网页 chrome 插件爬取下来的网页只是一个 JSON 文件。

之所以不在插件里面处理，而在本地的命令行环境中处理，是为了更好的扩展性。

提供了一个强大的命令行工具来帮助你处理 JSON 数据，让他们可以在 Markdown 显示出来。

两个 npm script:

| 命令        | 功能       |
| ----------- | ---------- |
| npm install | 初始化     |
| npm start   | 运行命令行 |

随着程序的多次运行，你可能会对文件的杂乱感到不舒服，clean.js 的作用就在于此。它有三个参数。

| 参数 | 作用             |
| ---- | ---------------- |
| -o   | 删除 origin 文件 |
| -d   | 删除 data 文件   |
| -v   | 删除 view 文件   |

使用 `node clean.js` ，默认情况下会删除所有的内容，也就是和`node clean.js -dov`等价。
