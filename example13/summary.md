#习题13
---
* 利用import导入库
* argv是让用户在命令行输入参数，不同于raw_input(),它是让用户在脚本执行的过程中输入参数
* argv就是所谓“参数变量”这个变量包含了你传递给python的参数
<pre><code>script, first, second, third = argv
</code></pre>
**这句的意思是把argv中的东西解包，将所有的参数依次赋予左边的变量名**