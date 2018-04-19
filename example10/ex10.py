# -*- coding: utf-8 -*-
'''
Created on Tue Apr 17 20:23:00 2018

@author: tm
'''
a = "I am 6'2\" tall." #将字符串中的双引号转义
b = 'I am 6\'2" tall.' #将字符串中的单引号转义
print a + '\n', b

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line"
backslash_cat = "I'm \\ a \\ cat"

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat