#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 26 15:33:11 2022

@author: ilariacaporali
"""

import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return -2 + x + np.exp(-x) + np.sin(x*x)

def f_r(x):
    return 2 - np.exp(-x) -np.sin(x*x)


#main
xguess = 2
tol=1e-5
x=0

while(abs(x-xguess)>tol):
    x = f_r(xguess)
    xguess = x
    
print(x)


x = np.linspace(-2,3, 10000)
zeross = np.zeros(len(x), float)
plt.plot(x, f(x), label='f(x)')
plt.plot(x, zeross, linestyle=':', label='zero')
plt.grid()
plt.legend()
plt.show()