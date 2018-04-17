# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 11:13:06 2018

@author: tm
"""

formatter = "%r %r %r %r"
print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
        "I had this thing.",
        "That you could type up right.",
        "But it didn't sing.",
        "So I said goodnight."
)