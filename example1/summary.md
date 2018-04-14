#习题1
---
* python基础的打印语句  
* 注意python2和python3的语法区别  
###python2中print的语法  
>python2中print是一个语法结构.  
  
python2打印时可以不加括号：   

`print 'Hello World'` 
###python3中print的语法 
>python3中print是一个内置函数，有多个参数

python3需要加括号  

`print("Hello World")`  

>`print(value1, ..., sep=' ', end='\n', file=sys.stdout, flush=False)`  
>* print可以支持多个参数，支持同时打印多个字符串（其中...表示任意多个字符串）；  
>* sep表示多个字符串之间使用什么字符连接；  
>* end表示字符串结尾添加什么字符，指点该参数就可以轻松设置打印不换行，Python2.x下的print语句在输出字符串之后会默认换行，如果不希望换行，只要在语句最后加一个“，”即可。但是在Python 3.x下，print()变成内置函数，加“，”的老方法就行不通了。    
>* **Python2打印时可以不加括号：print 'hello world'， Python3则需要加括号   print("hello world")
python3中print必须使用括号，因为它就是一个函数。**
