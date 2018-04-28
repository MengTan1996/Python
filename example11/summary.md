#习题11
---
* print语句最后加一个逗号,这样print就不会输出新的换行符而结束这一行跑到下一行去
* 输入身高6'22'' 输出结果为6\'22"  \用来转义单引号从而防止它被识别成字符串的结尾
###input()和raw_input()的区别
**Python3.x版本中已经丢弃了raw_input(),只有input()**   

* raw_input()将所有输入作为**字符串**看待,返回字符串类型
* input()只能接受**数字**,在对待纯数字时具有自己的特性,它返回输入的数字类型(int,float)  
* 在python3.x中raw_input()和input()进行了整合,去除了raw_input(),仅保留了input()函数,其接受任意输入,将所有输入默认为字符串处理,并返回字符串类型

####例子
<pre><code>
x = raw_input("please input a number:")
#x = input("please input a number:")
y = raw_input("please input a number:")
#y = input("please input a number:")
if x>=y:
    print x
else:
    print y
</code></pre>
**用raw_input()输入3456,20000结果是3456,其本质是比较的根本在于比较二者的ASCII码值，所以当输入x=3456,y=20000时，计算机就会按顺序一位一位地比较二者的ASCII码值，所以才会输出3456**
