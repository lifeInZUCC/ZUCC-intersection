## 关于命令行的解释

### 安装依赖

```shell
$ npm install
```

这个命令是 npm 用来安装包的，观察 package.json 文件你会发现，定义了一个 postinstall 的脚本，命令是 `node init.js`，它会在正常的安装之后做一些初始化.

相当于其实你运行 `npm install` 的时候不仅运行了原生的 `install package` 功能，也运行了 init.js 脚本。

### 运行程序

```
$ npm start
```

这条命令只是运行了 index.js 这个文件，与使用 `node index` 的效果完全一样，也就是直接运行或者调试 index.js 文件完全一样。

### 清空

```shell
$ node clean
```

由于一些设计上的缺陷，我们的程序会让文件呈指数倍的增长，所以我们提供了这个命令来更好的管理文件。

默认状态下会删除所有 data 目录下的文件。

仅删除 data/origin 目录。

```shell
$ node clean -o
```

仅删除 data/data 目录。

```shell
$ node clean -d
```

仅删除 data/view 目录。

```shell
$ node clean -v
```

删除 data/data 和 data/view 目录。

```shell
$ node clean -dv
```

你应该意识到，有一种写法和默认写法的功能重叠。

```shell
$ node clean -dov
```

---

## 设计与概念

### 文件模式

文件模式其实是一种文件的存在形式，目前拥有三种模式，`origin`、`data`、`view`。

### origin

origin模式的文件应该以`.txt`结尾。同时还需要遵守一定的格式，例如:

单选题

```
1.世界上最好的语言是什么?
A.PHP
B.Java
C.Javascript
D.C++
A
```

多选题

```
2.世界上最好的语言是什么?
A.PHP
B.Java
C.Javascript
D.C++
A B C D
```

填空题

```
3.世界上最好的语言是什么?
PHP
```

判断题

```
4.世界上最好的语言是PHP吗?
A.T
B.F
A
```

### data

data模式的文件应该以`.json`结尾。另外，里面的内容还需要满足一定的格式，例如：

单选题

```json
{
	"title": "世界上最好的语言是什么?",
	"choice": [
		{
			"option": "A",
			"content": "PHP"
		},
		{
			"option": "B",
			"content": "Java"
		},
		{
			"option": "C",
			"content": "Javascript"
		},
		{
			"option": "D",
			"content": "C++"
		}
	],
	"answer": "A"
}
```

多选题

```json
{
	"title": "世界上最好的语言是什么?",
	"choice": [
		{
			"option": "A",
			"content": "PHP"
		},
		{
			"option": "B",
			"content": "Java"
		},
		{
			"option": "C",
			"content": "Javascript"
		},
		{
			"option": "D",
			"content": "C++"
		}
	],
	"answer": "A B C D"
}
```

填空题

```json
{
	"title": "世界上最好的语言是什么?",
	"answer": "PHP"
}
```

判断题

```json
{
	"title": "世界上最好的语言是PHP吗?",
	"choice": [
		{
			"option": "A",
			"content": "T"
		},
		{
			"option": "B",
			"content": "F"
		}
	],
	"answer": "A"
}
```

### view

view 理论上只要是满足 Markdown 语法要求的列表就行了，一般我不推荐直接写 view .

因为这样的 Markdown 写起来比较麻烦，相对来说 origin 格式的最容易编写，我推荐自己编写origin 格式。或者使用网页上爬取下来的 data 格式。

然后把放到相应的目录下，运行 `npm start` 就可以在 data/view 目录下找到你的题目文件了。

大多数博客平台都兼容 markdown 的语法，基本上直接复制进去就好了。

## 配置

exercises-manager 提供了非常多的可定制的配置。

所有的配置信息都在 config.json 中。

### 自定义存储目录

我们之前都是 origin 类型的文件对应了 data/origin 目录，data 类型的文件对应了 data/data 目录，view 类型的文件对应了 data/view 目录。

其实这些目录的具体路径都是能改的，只不过还是只能在 data 目录下，这是为了防止混乱，请体谅。

例如，找到 config.json，修改默认存储路径 data/origin 为 data/txt。

```json
"origin": {
    "storage": "txt"
}
```

### 自定义文件后缀名

我们之前一直都说 origin 文件必须是 txt，data 文件必须是 json，view 文件必须是 md。

其实，不然，修改template属性就可以。

```json
"origin": {
    "template": "md"
}
```

这可能会引起一些混乱，一般情况下就别去使用了。

### 关闭转换通道

如果你不想要 data 文件转到 view 文件，可以尝试关闭通道，通过设置 switch 属性。

```json
"data": {
    "switch": false
}
```

### 添加额外的目录

使用浏览器下载的 json 文件 难道要每一次都复制到 data/data 下然后转换吗？

不需要，可以把浏览器的默认下载路径放到 extra 属性里面。

extra属性有两个可选的选项。file是单个文件的导入，dir是一个目录的导入。

例如，我习惯这样写:

```json
"data": {
    "extra": {
		"file":[],
		"dir":["/Users/jayceechow/Downloads"]
	}
}
```

不同系统的路径肯定不一样，linux和mac应该都是这种风格的。

windows 一般是 `C:\\Users\\jayceechow\\Downloads`。

之所以有两个反斜杠是因为一个反斜杠一般是转义的意思。

### 编写view样式

我们最终是把所有的内容都转换成 md 的，但是如果我们不想要默认的 md 格式怎么办，总不可能一个个去改，修改 viewformat 属性可以解决。

```json
"viewformat": {
	"size": "middle",
	"align": "left",
	"color": "red"
}
```

##### size

size有三个可取值，small、middle、large。

这个属性会改变最终显示的标题的文字大小，事实上这三个值分别对应了 md 的语法 `####` `###` `##`，也即是通过改变标题的级别来造成影响。

##### align

大部分题型在最终的 md 文件里面都是用表格的语法来完成的，表格有多种对齐方式，分别是 left、right、middle。

一般题目的选项都是表格语法，所以，你可以设置这三个属性来决定选项的对齐方式。

##### color

正确答案会被标记，标记的颜色可以通过改变这个属性来完成，默认的是red。

你需要了解HTML或者说CSS中颜色的设置格式。
