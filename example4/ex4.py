# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 14:03:40 2018

@author: tm
"""
cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car =passengers / cars_driven
#错误信息处在car_pool_capacity该变量未定义，应该为carpool_capacity
#average_passengers_per_car = car_pool_capacity / passenger 

#code with python2
print "There are",cars,"cars available."
print "There are onle",drivers,"drivers available."
print "There will be",cars_not_driven,"empty cars today."
print "We can transport",carpool_capacity,"people today." 
print "We have",passengers,"to carpool today."
print "We need to put about",average_passengers_per_car,"in each car."

"""
code with python3
print("There are",cars,"cars available.")
print("There are onle",drivers,"drivers available.")
print("There will be",cars_not_driven,"empty cars today.")
print("We can transport",carpool_capacity,"people today." )
print("We have",passengers,"to carpool today.")
print("We need to put about",average_passengers_per_car,"in each car.")
"""