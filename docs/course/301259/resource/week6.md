### 1.Consider the following three threads in a concurrent program that uses semaphores Sem1, Sem2, and Sem3.What are the initial values that can be given to the semaphores so that the threads cooperate to print a string that begins with 162162162162162?

```
Thread 1
L1: sema_down(Sem1);
  print("6");
  sema_up(Sem2);
goto L1;

Thread 2
L2: sema_down(Sem2);
  print("2");
  sema_up(Sem3);
goto L2;

Thread 3
L3: sema_down(Sem3);
  print("1");
  sema_up(Sem1);
goto L3;
```

|编号|选项|
|:-|:-|
|A|sem1=0, sem2=0, sem3=0|
|B|sem1=1, sem2=1, sem3=1|
|C|sem1=0, sem2=1, sem3=0|
|<font color="red">D</font>|<font color="red">sem1=0, sem2=0, sem3=1</font>|
