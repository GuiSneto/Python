# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 17:45:15 2019

@author: Guilherme
"""

import numpy as np
import matplotlib.pyplot as plt

n = 30
dt = 0.1 # s
g = 9.81 # m / s2
gamma = 0.5
x0 = 0
v0 = 0

def free(x,v, dt): 
    dv = v + dt*(g-gamma*v**2)  
    dx = x + dt*v
    return dx, dv

def step(x,v,dt):
    dx, dv = free(x,v, dt)
    v = v0 + dv
    x = x0 + dx
    return x, v

def euler(x0, v0, dt, n):
    x = (n + 1)*[0]
    v = (n + 1)*[0]
 
    for i in range(n):
        x[i + 1], v[i + 1] = step(x[i],v[i],dt) 
    
    return x, v

def plot():
    t = np.linspace(0, 10, n + 1)
    x,v = euler(x0, v0, dt, n)
    axes_height = plt.subplot(211)
    plt.plot(t,x)
    axes_velocity = plt.subplot(212)
    plt.plot(t,v)
    axes_height.set_ylabel('Posicao em m')
    axes_velocity.set_ylabel('Velocidade em m/s')
    axes_velocity.set_xlabel('Tempo em s')
    plt.show() 

plot()
