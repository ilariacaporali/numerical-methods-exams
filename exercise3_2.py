#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 10:26:12 2022

@author: ilariacaporali
"""

import numpy as np
import matplotlib.pyplot as plt
from numpy.random import random, seed
seed(17)

def f(x):
    return np.sin(x) * (1-x)**2

#main
h =0.01
n = int(np.pi/h)
xmax = np.pi
xmin = 0
xl = np.linspace(xmin, xmax, n)
'''
plt.plot(xl, f(xl), color='cornflowerblue')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.show()
'''
N = np.array( [int(1e3), int(1e4), int(1e5), int(1e6) ] )

I = np.zeros(len(N), float)

#N=1e3
a3 = random(N[0])
x3 = xmax*a3

for i in range(N[0]):
    I[0] += (xmax-xmin) * f(x3[i]) / N[0]
        
#N=1e4
a4 = random(N[1])
x4 = xmax*a4

for i in range(N[1]):
    I[1] += (xmax-xmin) * f(x4[i]) / N[1]
        
#N=1e5
a5 = random(N[2])
x5 = xmax*a5

for i in range(N[2]):
    I[2] += (xmax-xmin) * f(x5[i]) / N[2]
        
        
#N=1e6
a6 = random(N[3])
x6 = xmax*a6

for i in range(N[3]):
    I[3] += (xmax-xmin) * f(x6[i]) / N[3]
        
plt.plot(np.log10(N), I, marker = 'h', color='cornflowerblue', label='Integral value (mean value method)')
plt.xlabel('$log_{10}N$')
plt.ylabel('I')
plt.legend()
#plt.xscale('log')
plt.show()


        









    




