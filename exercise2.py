#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 09:48:12 2022

@author: ilariacaporali
"""

def inverse(x, c, a, Tmin, Tmax):
    return ( (1-a)*x/c + Tmin**(1-a) )**(1/(1-a))

def p(x_line, c, a):
    return c * (x_line**(-a))

import numpy as np
import matplotlib.pyplot as plt
from numpy.random import random, seed

seed(137)

N = int(1e6)
Tmin = 0.15
Tmax = 5.5
a = 0.55

c = (1-a)/( Tmax**(1-a) - Tmin**(1-a)  )

x = random(N)

T = inverse(x, c, a, Tmin, Tmax)

mybins = np.logspace(np.log10(Tmin), np.log10(Tmax), 50 )

x_line = np.linspace(Tmin, Tmax, 10000)

plt.hist(T, bins= mybins, density=True, histtype='step', log=True, color='darkmagenta', label='hist')
plt.xscale('log')
plt.yscale('log')
plt.plot(x_line, p(x_line, c, a), color='cornflowerblue', linestyle=':', label='$y \propto x^{-0.55}$')
plt.legend()
plt.show()


