# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 01:05:29 2019

@author: Guilherme
"""

import numpy as np

def baskara(a,b,c):
    d = ((b^2) - 4*a*c + 0.0j)
    x = (-b+np.sqrt(d+0j))/2*a
    y = (-b-np.sqrt(d+0j))/2*a
    
    return(x,y)

