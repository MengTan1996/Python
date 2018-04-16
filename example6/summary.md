#习题6：字符串和文本
---
* %r和%s的不同  
  >用%r显示的是变量“原始”的数据值，%r在打印的时候能够重现它代表的对象，但其他的符号用来给用户显示变量值。  
  >例子：  
  ><pre><code>text = "I am %d years old." % 22
print "I said: %s." % text
print "I said: %r." % text  
</code></pre>
返回的结果：
><pre><code>I said: I am 22 years old..
I said: 'I am 22 years old.'. // %r 给字符串加了单引号
</code></pre>

* <pre><code>w = "This is the left side of..."
e = "a string with a right side."
print w + e
</code></pre>
返回的结果：
`This is the left side of...a string with a right side.`  
**用+连起来 w 和 e 就可以生成一个更长的字符串。**