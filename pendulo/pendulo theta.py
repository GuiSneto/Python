# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 15:10:42 2019

@author: Guilherme
"""
import numpy as np
import matplotlib.pyplot as plt

g = 9.81    # m/s^2. Gravitational acc
m = 1.      # kg. Mass
L = 1.      # m. Length of rod
w0 = 1     # 1/s. Initial angular velocity
theta0 = 3. # rad. Initial angle
T = 20.     # s. Time of simulation
n = 100000  # Number of steps
b = .5      # kg m. Damping factor
dt = T/float(n)


def RHS(theta, w, dt):
    dw = -np.sin(theta)*dt*g/L - b/(L*m)*w*dt
    dtheta = w*dt
    return dtheta, dw

def euler_step(theta, w, dt):
    dtheta, dw = RHS(theta, w, dt)
    w = w + dw
    theta = theta + dtheta
    return theta, w

def euler_method(theta0, w0, dt, n):
    theta = (n + 1)*[0]
    w = (n + 1)*[0]
    
    theta[0] = theta0
    w[0] = w0
    for i in range(n):
        theta[i + 1], w[i + 1] = euler_step(theta[i], w[i], dt) 
    
    return theta, w

def plot():
    t = np.linspace(0, T, n + 1)
    theta,w = euler_method(theta0, w0, T/float(n), n)
    plt.title("Angular position")
    plt.plot(t, w, "m")
    plt.xlabel(r"$t$, [s]")
    plt.ylabel(r"$\theta(t)$, [rad]")
    plt.show()

plot()


