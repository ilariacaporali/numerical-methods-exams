#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 26 10:04:26 2022

@author: ilariacaporali
"""

import numpy as np
import matplotlib.pyplot as plt
from cmath import exp

def user_dft(y):
    N = len(y)
    c = np.zeros(N//2+1, complex)
    
    for k in range(len(c)):
        for n in range(N-1):
            c[k] += y[n]* exp(-2j*np.pi *k*n /N)
            
    return c

def find_max(c):
    c_max = 0
    k_max = 0
    for k in range(1,len(c)):
        if(c[k]>c_max):
            c_max = c[k]
            k_max = k
            
    return k_max, c_max
        

#main

t, y = np.genfromtxt('fourierA.txt', dtype='float', usecols=(0,1), skip_header = 1, unpack = True)

'''
plt.plot(t, y, color='red', label='signal')
plt.xlabel('t')
plt.ylabel('y(t)')
plt.show()
'''
N = len(y)
print(N)

c_k = np.fft.rfft(y)
c_k = abs(c_k)
print(len(c_k))

c = user_dft(y)

c = abs(c)

k_max, c_max = find_max(c_k)
print(k_max, c_max)

nu = k_max/N
T = 1/nu

print(T)





plt.plot(c_k, color='blue', label='fft.rfft')
plt.plot(c, color='orange', linestyle=':', label='dft (user)')
plt.xlabel('k')
plt.ylabel('|c_k|')
plt.legend()
plt.show()
