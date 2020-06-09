作为一位深度 VSCode 用户，我强烈推荐把 VSCode 作为电脑上所有代码的编辑器。

[vscode 下载链接](https://code.visualstudio.com/)

就本项目的编辑而言，推荐安装的插件有:

-   两款美化插件`One Dark Pro`+`Material Icon Theme`。
-   一款 Markdown 扩展`Markdown All in One`，支持一些语法。（必装）
-   一款 Markdown 格式化工具，准确来说是基本支持所有语言了，叫`Pretter`。
-   项目管理插件`Project Manager`。把自己的项目保存在这里，下次打开编辑器就可以直接找到了。

关于 vscode 的 markdown 编辑工作，我给一个我自己的配置。但是不是必须的，就算不配置也够用，只是个人习惯和开发效率问题。

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
