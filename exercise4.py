#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 26 10:26:24 2022

@author: ilariacaporali
"""

import numpy as np
import matplotlib.pyplot as plt
from numpy.random import random, seed

seed(137)

def solvec1c2(m_min, m_max, mc, a1, a2):
    A = ( mc**(1-a1) - m_min**(1-a1) ) / (1-a1)
    B = ( m_max**(1-a2) - mc**(1-a2) ) / (1-a2)
    C = mc**(-a1)
    D = -mc**(-a2)
    l0 = np.array([A, B])
    l1 = np.array([C, D])
    mat = np.array([l0, l1])
    b = np.array([1., 0.])
    
    sol = np.linalg.solve(mat, b)
    
    return sol[0], sol[1]

def xcritical1(c1, a1, mc, m_min):
    return c1 * ( mc**(1-a1) - m_min**(1-a1) ) / (1-a1)

def xcritical2(c2, a2, mc, m_max):
    return 1 - c2 * ( m_max**(1-a2) - mc**(1-a2) ) / (1-a2)

def inverse1(c1, a1, m_min, x):
    return ( (1-a1)*x/c1 + m_min**(1-a1) )**(1/(1-a1))

def inverse2(c2, m_max, a2, x):
    return ( m_max**(1-a2) - (1-a2)*(1-x)/c2 )**(1/(1-a2))

def f1(x1, c1, a1):
    return c1*x1**(-a1)

def f2(x2, c2, a2):
    return c2*x2**(-a2)
       
#main

m_min = 0.1
m_max = 150
mc = 1.18
a1 = 1.1
a2 = 1.6

c1, c2 = solvec1c2(m_min, m_max, mc, a1, a2)

N = int(1e6)

xc = xcritical1(c1, a1, mc, m_min)

x = random(N)
y = np.zeros(N, float)

for i in range(N):
    if( x[i] < xc ):
        y[i] = inverse1(c1, a1, m_min, x[i])
    else:
        y[i] = inverse2(c2, m_max, a2, x[i])
        
x1 = np.linspace(m_min, mc, 10000)
y1 = f1(x1, c1, a1)

x2 = np.linspace(mc, m_max, 10000)
y2 = f2(x2, c2, a2)
 
mybins = np.logspace(np.log10(m_min), np.log10(m_max), 100)
plt.hist(y, bins=mybins, density=True, histtype='step', log=True, label='hist')
plt.plot(x1, y1, color='red', label='$y \propto m^{-1.1}$')
plt.plot(x2, y2, color='green', label='$y \propto m^{-1.6}$')
plt.xscale('log')
plt.yscale('log')
plt.xlabel('m')
plt.ylabel('PDF')
plt.legend()
plt.show()
        







