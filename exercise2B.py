#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 26 15:44:42 2022

@author: ilariacaporali
"""

import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return -2 + x + np.exp(-x) + np.sin(x*x)

def bisection_method(x1, x2):
    tol = 1e-3
    print(f(x1))
    print(f(x2))
    
    while( abs(x1-x2) > tol ):
        midpoint = 0.5*(x1+x2)
        if( ( f(x1)>0 and f(midpoint)>0 ) or ( f(x1)<0 and f(midpoint)<0 ) ):
            x1 = midpoint
        else:
            x2 = midpoint
    return 0.5*(x1+x2)

#main

#1st sol

sol1 = bisection_method(-0.8, -0.6)
print('1st sol = ', sol1)

sol2 = bisection_method(0.8, 0.92)
print('2nd sol = ', sol2)

sol3 = bisection_method(1.7, 1.8)
print('3rd sol = ', sol3)

sol4 = bisection_method(2.3, 2.45)
print('4th sol = ', sol4)



x = np.linspace(-2,3, 10000)
zeross = np.zeros(len(x), float)
plt.plot(x, f(x), label='f(x)')
plt.plot(x, zeross, linestyle=':', label='zero')
plt.grid()
plt.legend()
plt.show()