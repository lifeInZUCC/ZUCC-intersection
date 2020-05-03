## 内联代码高亮

一般在 markdown 里面，代码块可以高亮，但是内联的代码却不是高亮的。我们的引擎提供了这个功能。

例如: 

```
`#!js var test = 0;`
```

结果: `#!js var test = 0;`


## 显示行号

添加一个 `linenums="1"` 的参数，开启行号的显示。

例如:

<pre>
<code>
&lsquo;&lsquo;&lsquo; python linenums="1"
def bubble_sort(items):
    for i in range(len(items)):
        for j in range(len(items) - 1 - i):
            if items[j] > items[j + 1]:
                items[j], items[j + 1] = items[j + 1], items[j]
&lsquo;&lsquo;&lsquo;
</code>
</pre>

结果: 

``` python linenums="1"
def bubble_sort(items):
    for i in range(len(items)):
        for j in range(len(items) - 1 - i):
            if items[j] > items[j + 1]:
                items[j], items[j + 1] = items[j + 1], items[j]
```

## 标记代码

添加一个 `hl_lines="行号"` 参数，凸显标记代码。

例如:

<pre>
<code>
&lsquo;&lsquo;&lsquo; python hl_lines="3 4"
def bubble_sort(items):
    for i in range(len(items)):
        for j in range(len(items) - 1 - i):
            if items[j] > items[j + 1]:
                items[j], items[j + 1] = items[j + 1], items[j]
&lsquo;&lsquo;&lsquo;
</code>
</pre>

结果:

``` python hl_lines="3 4"
def bubble_sort(items):
    for i in range(len(items)):
        for j in range(len(items) - 1 - i):
            if items[j] > items[j + 1]:
                items[j], items[j + 1] = items[j + 1], items[j]
```

!!! tip
    `hl_lines`和`linenums`连用的效果不错。

## 代码组

面对一道有许多解法的题目，我们提供了代码组的功能，可以在任意语言中切换。

例如:

<pre>
<code>
&lsquo;&lsquo;&lsquo; python tab="Bash"
#!/bin/bash

echo "Hello world!"
&lsquo;&lsquo;&lsquo;
</code>
<code>
&lsquo;&lsquo;&lsquo; c tab="C"
#include <stdio.h>

int main(void) {
  printf("Hello world!\n");
}
&lsquo;&lsquo;&lsquo;
</code>
<code>
&lsquo;&lsquo;&lsquo; cpp tab="C++"
#include <iostream>

int main() {
  std::cout << "Hello world!" << std::endl;
  return 0;
}
&lsquo;&lsquo;&lsquo;
</code>
<code>
&lsquo;&lsquo;&lsquo; c# tab="C#"
using System;

class Program {
  static void Main(string[] args) {
    Console.WriteLine("Hello world!");
  }
}
&lsquo;&lsquo;&lsquo;
</code>
</pre>

结果：

``` bash tab="Bash"
#!/bin/bash

echo "Hello world!"
```

``` c tab="C"
#include <stdio.h>

int main(void) {
  printf("Hello world!\n");
}
```

``` c++ tab="C++"
#include <iostream>

int main() {
  std::cout << "Hello world!" << std::endl;
  return 0;
}
```

``` c# tab="C#"
using System;

class Program {
  static void Main(string[] args) {
    Console.WriteLine("Hello world!");
  }
}
```

## diff代码

使用diff关键字，会出现类似与git的显示效果，显示代码的差异。

例如:

<pre>
<code>
&lsquo;&lsquo;&lsquo; diff
Index: grunt.js
===================================================================
--- grunt.js    (revision 31200)
+++ grunt.js    (working copy)
@@ -12,6 +12,7 @@

 module.exports = function (grunt) {

+  console.log('hello world');
   // Project configuration.
   grunt.initConfig({
     lint: {
@@ -19,10 +20,6 @@
         'packages/services.web/{!(test)/**/,}*.js',
         'packages/error/**/*.js'
       ],
-      scripts: [
-        'grunt.js',
-        'db/**/*.js'
-      ],
       browser: [
         'packages/web/server.js',
         'packages/web/server/**/*.js',
&lsquo;&lsquo;&lsquo;
</code>
</pre>

结果:

```diff
Index: grunt.js
===================================================================
--- grunt.js    (revision 31200)
+++ grunt.js    (working copy)
@@ -12,6 +12,7 @@

 module.exports = function (grunt) {

+  console.log('hello world');
   // Project configuration.
   grunt.initConfig({
     lint: {
@@ -19,10 +20,6 @@
         'packages/services.web/{!(test)/**/,}*.js',
         'packages/error/**/*.js'
       ],
-      scripts: [
-        'grunt.js',
-        'db/**/*.js'
-      ],
       browser: [
         'packages/web/server.js',
         'packages/web/server/**/*.js',
```
