# -*- coding: utf-8 -*-
"""
Created on Sat Apr 28 15:26:01 2018

@author: TM
"""

from sys import argv

script, filename = argv

#txt变量的值是open()函数返回的文件对象
txt = open(filename)

print "Here's your file %r:" %filename
print txt.read();
print "Type the filename again:"
file_again = raw_input(">")
txt_again = open(file_again)
print txt_again.read()