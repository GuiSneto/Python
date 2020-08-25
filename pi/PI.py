# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 19:17:38 2019

@author: Guilherme
"""
import matplotlib.pyplot as plt
from numpy import random
def calpi():
    n = 100000
    dentro = fora = 0
    x = random.rand(n)  
    y = random.rand(n)
    for i in range(0,n):
        if (x[i]**2) + (y[i]**2) <= 1:
            dentro += 1
        else:
            fora += 1
    k = 4*dentro/n
    print(k)
def showpi():
    n = 1000
    x = random.rand(n)  
    y = random.rand(n)
    for i in range(0,n):
        if (x[i]**2) + (y[i]**2) <= 1:
            plt.scatter(x[i],y[i],color = 'b') 
        else:
            plt.scatter(x[i],y[i],color = 'y')
    plt.show()
    
#######################################################################