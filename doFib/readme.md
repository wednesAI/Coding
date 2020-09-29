测试代码是递归版本的斐波那契数列计算函数

1，在Python的代码实现如下：

![image-20200928203427743](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20200928203427743.png)

运行了5遍，效率表现如下：

![image-20200928203820498](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20200928203820498.png)

2，在Golang的代码实现如下：

![image-20200928203931105](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20200928203931105.png)

运行了5遍，效率表现如下;

![image-20200928204026664](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20200928204026664.png)

3,此时，我修改fib.go，使之能用gcc来编译，代码如下：

![image-20200928204146064](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20200928204146064.png)

//export Fib是必须加的，因为在编译成.so文件时，编译器会寻找这个注释，为了能正常编译，必须导入C这个包，同时函数名是大写的，在Golang中，只有首字母大写的函数，才能被package外部的代码调用，接着运行（此时需要注意电脑有无安装gcc编译器）如下命令进行编译：

​	go build -buildmode=c-shared -o _fib.so fib.go

同目录下产生两个文件（.h由cgo生产，不可编辑，.so是十六进制文件）：

![image-20200928204916457](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20200928204916457.png)

4，这个时候可以重写py文件，修改成如下：

![image-20200928205135213](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20200928205135213.png)

ctypes是Python内置模块，用来加载.so文件，并提取里边Fib函数

看下最终执行了5遍的效果：

![image-20200928205417795](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20200928205417795.png)

5，参考资料：

https://golang.org/cmd/cgo

6，总的来说，通过Python去调用Golang的代码，能将效率提高很多。