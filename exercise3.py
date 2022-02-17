#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 28 09:48:30 2022

@author: ilariacaporali
"""

import numpy as np
import matplotlib.pyplot as plt
import astropy.constants as constants

def f(x):
    return 5*np.exp(-x) + x -5

def bisection(x1, x2, tol):
    
    while(abs(x1-x2)>tol):
        midpoint = 0.5*(x1+x2)
        if (f(x1)>0 and f(midpoint)>0) or (f(x1)<0 and f(midpoint)<0):
            x1 = midpoint
        else:
            x2 = midpoint
            
    xsol = 0.5*(x1+x2)
    print(xsol)
    return xsol

    

#main

tol = 1e-5

x = np.linspace(-1, 6, 1000)
y = f(x)
zeross=np.zeros(1000, float)

x1sol =  bisection(-1, 1, tol)
x2sol =  bisection(4, 6, tol) #i think only this has a physical meaning


print('b_wien (astropy) = ', constants.b_wien)

b = constants.h * constants.c / (constants.k_B * x2sol) 

print('b_wien (calculated) = ', b )


plt.plot(x, y, color='blue')
plt.plot(x, zeross, color='red', linestyle=':')
plt.show()


