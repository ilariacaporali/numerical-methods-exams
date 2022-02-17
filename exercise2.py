#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 26 09:42:32 2022

@author: ilariacaporali
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import scipy.optimize as opt

def func(x,a, b):
    return a + b*x

def user_fit(x, y):
    N = len(x)
    x_mean = np.mean(x)
    y_mean = np.mean(y)
    
    num=0
    den=0
    sum_x = 0
    sum_xx = 0
    
    for i in range(N):
        num += y[i]*(x[i] - x_mean) 
        den += x[i]*(x[i] - x_mean) 
        sum_x += x[i]
        sum_xx += x[i]*x[i]
        
    B = num/den
    A = y_mean - x_mean*B
    D = N *sum_xx - sum_x*sum_x
    
    res = 0
    
    for i in range(N-1):
        res += (y[i] - A - B*x[i])*(y[i] - A - B*x[i])
        
    sy = np.sqrt(res/(N-1))
    
    sA = sy * np.sqrt(sum_xx /D)
    sB = sy * np.sqrt(N/D)
    
    return A, B, sA, sB
                    
#main

M, R = np.genfromtxt('BBH_EAGLE25Mpc_z01.txt', dtype='float', skip_header=1, usecols=(0,1), unpack=True)

log_M = np.log10(M)
log_R = np.log10(R)

popt, pcov = opt.curve_fit(func, log_M, log_R)

A, B, sA, sB = user_fit(log_M, log_R)

x_line = np.linspace(min(log_M), max(log_M), 10000)
y_line = func(x_line, popt[0], popt[1])
y_line_user = func(x_line, A, B)

print('y = a + bx')
print('scipy')
print ('a = ', popt[0], ' +/- ', pcov[0,0])
print ('b = ', popt[1], ' +/- ', pcov[1,1])
print('user fit')
print ('a = ', A, ' +/- ', sA)
print ('b = ', B, ' +/- ', sB)


plt.scatter(log_M, log_R, marker='*', color='black', label='data')
plt.plot(x_line, y_line, color='deeppink', label ='curve_fit')
plt.plot(x_line, y_line_user, linestyle=':', color='cyan', label ='user fit')
plt.xlabel('$ log_{10}(M) \;  [M_{\odot}] $')
plt.ylabel('$ log_{10}(R_{BBH}) \; [Gyr^{-1]}$')
plt.legend()
plt.show()



