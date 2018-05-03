# -*- coding: utf-8 -*-
"""
Created on Sat Apr 28 15:02:06 2018

@author: TM
"""

from sys import argv

script, user_name = argv
prompt = '>'

print "Hi %s, I'm the %s script." %(user_name, script)
print "I'd like to ask you a few question."
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "Where do you live %s?" %user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
""" %(likes, lives, computer)

#python ex14.py tm
#argv只能在命令行模式下才能输入参数