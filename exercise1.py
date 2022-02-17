#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 28 09:09:48 2022

@author: ilariacaporali
"""

def func(x, a, b):
    return a + b*x

#main

import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as opt

m_bh, t_sn = np.genfromtxt('data_black_holes.txt', dtype = float, skip_header=3, usecols=(3,19), unpack=True)

log10_m = np.log10(m_bh)
log10_t = np.log10(t_sn)

popt, pcov = opt.curve_fit(func, log10_m, log10_t)

print('opt.curve_fit values : y = a + b*x')
print('a = ', popt[0], ' \pm ', pcov[0,0])
print('b = ', popt[1], ' \pm ', pcov[1,1])

x = np.linspace(min(log10_m), max(log10_m), 10000)
y = func(x, popt[0], popt[1])

plt.scatter(log10_m, log10_t, marker='*', color='black', label='data')
plt.plot(x, y, color='purple', label='y=a+bx')
plt.xlabel('$log_{10}(M_{BH}) \; \;  [M_{\odot}] $')
plt.ylabel('$log_{10}(t_{SN}) \; \;  [Myr] $')
plt.legend()
plt.show()