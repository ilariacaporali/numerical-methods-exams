#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 28 09:24:57 2022

@author: ilariacaporali
"""

import numpy as np
from numpy.random import random, seed 
import matplotlib.pyplot as plt

seed(12137)

N = int(1e5)

a = random(N)
b = random(N)
c = random(N)

xr = 2*a - 1.
yr = b - 0.5
zr = c - 0.5

xx = []
yy = []
zz = []

for i in range(N):
    if ( (xr[i]**2 + yr[i]**2 + zr[i]**2)**2 <= (xr[i]**2 - yr[i]**2 - zr[i]**2)  ):
        xx.append(xr[i])
        yy.append(yr[i])
        zz.append(zr[i])
        
xx = np.array(xx)
yy = np.array(yy)
zz = np.array(zz)

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

ax.scatter(xx, yy, zz, marker='*', color='green')

plt.show()

#integral

M = int(1e5)

ai = random(M)
bi = random(M)
ci = random(M)

xi = 2*ai - 1.
yi = bi - 0.5
zi = ci - 0.5

k = 0 #counter

for i in range(M):
    if ( (xi[i]**2 + yi[i]**2 + zi[i]**2)**2 <= (xi[i]**2 - yi[i]**2 - zi[i]**2)  ):
        k += 1
        
I = k*2/M

print(I)


        