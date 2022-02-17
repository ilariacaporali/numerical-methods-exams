#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 11:29:29 2022

@author: ilariacaporali
"""

import numpy as np
import matplotlib.pyplot as plt
from numpy.random import random, seed

seed(137)

def sphere(x, y, z):
    return x*x + y*y + z*z

#main

N =int(1e4)

a = random(N)
b = random(N)
c = random(N)

xr = a*10 - 5
yr = b*10 - 5
zr = c*10 - 5

x = []
y = []
z = []

for i in range(N):
    if( sphere(xr[i], yr[i], zr[i]) < 25 ):
        x.append(xr[i])
        y.append(yr[i])
        z.append(zr[i])
        
x = np.array(x)
y = np.array(y)
z = np.array(z)
'''
plt.scatter(x, y, marker='*')
plt.show()

'''
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.scatter(x, y, z, marker='*', label='random number inside a sphere')
plt.legend()
plt.show()
