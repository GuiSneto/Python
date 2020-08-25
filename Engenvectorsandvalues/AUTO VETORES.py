# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 15:33:01 2019

@author: Guilherme
"""

import numpy as np
def f(i,j):
    if i == j:
        return 2
    if np.abs(i-j) == 1:
        return -1
    else:
        return 0
        
xy = np.array([[f(x,y) for x in range(0,200,1)] for y in range(0,200,1)])


# Liner Algebra
from numpy import linalg as LA
import matplotlib.pyplot as plt
evals,evecs = LA.eigh(xy)
l = evecs[:, 0:3]
plt.plot(l**2)
