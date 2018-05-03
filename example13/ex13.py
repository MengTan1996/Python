# -*- coding: utf-8 -*-
"""
Created on Sat Apr 28 14:37:10 2018

@author:TM
"""

from sys import argv
#把argv中的东西解包，将所有的参数依次赋予左边的变量名
script, first, second, third = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third

#python ex13.py 1 2 3
#argv只能在命令行模式下才能输入参数