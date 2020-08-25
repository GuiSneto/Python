# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 15:36:45 2019

@author: Guilherme
"""

import numpy as np

def fact(n):
    x = 1
    i = 2
    while i <= n:
        x =x*i
        i= i+1
    return(x)
