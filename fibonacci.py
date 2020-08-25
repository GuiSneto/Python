# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 01:09:06 2019

@author: Guilherme
"""

def fibonacci(a):
    x,y = 0,1
    while y < a:
          x,y = y,x+y
          print(y)
          
fibonacci(10)