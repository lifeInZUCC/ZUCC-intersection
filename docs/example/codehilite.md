## 内联代码高亮
只需要在内联代码之前加入`#!`+语言，就可以在行内显示高亮的代码，比如`#!js var test = 0;`，它的源代码是：
```
#!js var test = 0;
```

## 标记行

例如下面的代码可以标记3、4两行：

代码

<pre>
<code>
&lsquo;&lsquo;&lsquo; python hl_lines="3 4"
""" Bubble sort """
def bubble_sort(items):
    for i in range(len(items)):
        for j in range(len(items) - 1 - i):
            if items[j] > items[j + 1]:
                items[j], items[j + 1] = items[j + 1], items[j]
&lsquo;&lsquo;&lsquo;
</code>
</pre>

效果

``` python hl_lines="3 4"
""" Bubble sort """
def bubble_sort(items):
    for i in range(len(items)):
        for j in range(len(items) - 1 - i):
            if items[j] > items[j + 1]:
                items[j], items[j + 1] = items[j + 1], items[j]
```

!!! tip
    在markdown的语言声明后面添加`hl_line`就可以高亮显示指定行。

## 代码块分组

先来看看效果：

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

由于某些原因不太方便放源代码，说明一下，就是在markdown原来语言声明的地方改成这样：`c++ tab="c++"`，tab里的内容就是最后显示在上面一栏的标签，前面的是语言声明。