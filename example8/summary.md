#习题8：打印打印
---
* <pre><code>print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
)
</code></pre>返回的结果
`'I had this thing.' 'That you could type up right.' "But it didn't sing." 'So I said goodnight.'`
输出语句的四句话都是双引号，为什么只有第三句话是双引号，其他都是单引号，%r打印时能够重现它所代表的对象。书中解释，因为%r常用来调试或检查，因此没必要将它输出的很漂亮。。仍存在疑问