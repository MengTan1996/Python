# -*- coding: utf-8 -*-
'''
Created on Fri Apr 20 9:30:00 2018

@author: tm
'''
#关于input() 和raw_input()的区别
x = raw_input()input("please input a number:")
#x = input("please input a number:")
y = raw_input("please input a number:")
#y = input("please input a number:")
if x>=y:
    print x
else:
    print y
# print "How old are you?",
# age = raw_input();
# print "How tall are you?",
# height = raw_input();
# print "How much do you weigh?",
# weight = raw_input();
#
# print "So, you're %r old,%r tall adn %r heavy." %(age, height, weight)