# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 14:26:39 2018

@author: tm
"""

name = 'Zed A. Shaw'
age = 35
height = 74
height_cm = height * 2.54
weight = 180
weight_kg = 180 * 0.4535924 
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." %(eyes, hair)
print "His teeth are usually %s depending on the coffee." %teeth
print "If I add %d, %d, and %d I get %d." %(age, height, weight, age + height + weight)
 
print "He's %d cm tall." % height_cm
print "He's %d kg heavy." % weight_kg