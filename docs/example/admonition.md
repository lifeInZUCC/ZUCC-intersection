## 几种显示用法
### 普通用法

代码:

```markdown
!!! note
    今天风和日丽。
```

结果:

!!! note
    今天风和日丽。

### 带标题用法

代码:

```markdown
!!! note "Jaycee Chow的日记"
    今天风和日丽。
```

结果:

!!! note "Jaycee Chow的日记"
    今天风和日丽。

### 无辩题用法

代码:

```markdown
!!! note ""
    今天风和日丽。
```

结果:

!!! note ""
    今天风和日丽。

### 可折叠用法

代码:

```markdown
??? note
    你看不见我。
```

结果:

??? note
    你看不见我。

## 几种显示类型
### Note

代码:

```markdown
!!! note
    今天风和日丽。
```

结果:

!!! note
    今天风和日丽。

note也可以用seealso替换。

### Abstract

代码:

```markdown
!!! abstract
    很久很久以前，巨龙突然出现，带来灾难，带走了公主又消失不见。王国十分危险，世间谁最勇敢，一位勇者赶来，大声喊，我要带上最好的剑，翻过最高的山，闯进最深的森林，把公主带回到面前。
```

结果:

!!! abstract
    很久很久以前，巨龙突然出现，带来灾难，带走了公主又消失不见。王国十分危险，世间谁最勇敢，一位勇者赶来，大声喊，我要带上最好的剑，翻过最高的山，闯进最深的森林，把公主带回到面前。

abstract也可以用summary或者tldr替换。

### Info

代码:

```markdown
!!! info
    操作系统作业没做完。
```

结果:

!!! info
    操作系统作业没做完。

info也可以用todo替换。

### Tip

代码:

```markdown
!!! tip
    程序员务必多喝芝麻，这样头发才会茂密。
```

结果:

!!! tip
    程序员务必多喝芝麻，这样头发才会茂密。

tip也可以用hint或者important替换。

### Success

代码:

```markdown
!!! success
    今日份的崩坏已肝完。
```

结果:

!!! success
    今日份的崩坏已肝完。

success也可以用check或者done替换。

### Question

代码:

```markdown
!!! question
    先有鸡还是先有蛋？
```

结果:

!!! question
    先有鸡还是先有蛋？

question也可以用help或者faq替换。

### Warning

代码:

```markdown
!!! warning
    warning: ignoring return value of ‘scanf’, declared with attribute warn_unused_result
```

结果:

!!! warning
    warning: ignoring return value of ‘scanf’, declared with attribute warn_unused_result

warning也可以用caution或者attention替换。

### Failure

代码:

```markdown
!!! failure
    Exception thrown  :java.lang.ArrayIndexOutOfBoundsException: 3
```

结果:

!!! failure
    Exception thrown  :java.lang.ArrayIndexOutOfBoundsException: 3

failure也可以用fail或者missing替换。

### Danger

代码:

```markdown
!!! danger
    高压电
```

结果:

!!! danger
    高压电

danger也可以用error替换。

### Bug

代码:

```markdown
!!! bug
    404 GET
```

结果:

!!! bug
    404 GET

无其他关键词可替换

### Example

代码:

```markdown
!!! example
    Admonition扩展语法关键词包括：

    Note，Abstract，Info，Tip，Success，Question，Warning，Failure，Danger，Bug，Example，Quote
```

结果:

!!! example
    Admonition扩展语法关键词包括：

    Note，Abstract，Info，Tip，Success，Question，Warning，Failure，Danger，Bug，Example，Quote

example也可以用snippet替换。

### Quote

代码:

```markdown
!!! quote
    Jeff Atwood: 一切能被JavaScript实现的终将会被JavaScript实现。 
```

结果:

!!! quote
    Jeff Atwood: 一切能被JavaScript实现的终将会被JavaScript实现。 