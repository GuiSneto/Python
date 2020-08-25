# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 20:41:43 2019

@author: Guilherme
"""
############################################################
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import numpy as np

G = 9.8
t = np.arange (0, 1.1, 0.1)
gamma = 0.5
x0 = 0

def veloc (v0,t,g):
    g = G
    vel = np.array ([0, 0,g])
    return vel

v0 = np.array ([1, 2, 0])
soln = odeint (veloc, v0, t, args = (G,))

fig = plt.figure (1, figsize = (8,8))


ax1 = fig.add_subplot(313)
ax1.plot(t, soln [:,2])
ax1.set_xlabel ('tempo')
ax1.set_ylabel ('V')

plt.show ()

def motion (x, t, g):
    posicao = np.array ([-g * t, -g])
    return posicao

v0 = np.array ([5.0, 0])
soln = odeint (motion, v0, t, args = (G,))

fig,axes = plt.subplots(1, 2)
fig.subplots_adjust(wspace=0.6)

axes[0].plot(t, soln [:,0])
axes[0].set_xlabel ('time')
axes[0].set_ylabel ('Sz')

axes[1].plot(t, soln [:,1])
axes[1].set_xlabel ('time')
axes[1].set_ylabel ('Vz')

plt.show ()




