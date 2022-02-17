#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 26 14:57:23 2022

@author: ilariacaporali
"""

import numpy as np
import matplotlib.pyplot as plt
from cmath import exp

def dft_user(y):
    N = len(y)
    c = np.zeros(N//2+1, complex)
    for k in range(len(c)):
        for n in range(N):
            c[k] += y[n] * exp(-2j*np.pi*k*n/N)
            
    c = abs(c)
    return c
    
def find_max(ck):
    k_max = 0
    ck_max = 0
    for k in range( 1,len(ck)):
        if(ck_max < ck[k]):
            ck_max = ck[k]
            k_max = k
    return k_max, ck_max
        

#main

t, y = np.genfromtxt('fourier.txt', dtype=float, skip_header=1, usecols=(0,1), unpack=True)
'''
plt.plot(t, y, label='signal')
plt.xlabel('t')
plt.ylabel('y(t)')
plt.legend()
plt.show()
'''
print(len(y))

c_k = np.fft.rfft(y)

c_k = abs(c_k)

print(len(c_k)) 

c= dft_user(y)
print(len(c))

k_max, c_max = find_max(c_k)

print(k_max, c_max)

nu = k_max/len(y)
T = 1/nu
k = np.linspace(0, len(c_k), len(c_k))
print(T)

plt.plot(c_k, label='numpy.fft.rfft')
plt.plot(c, linestyle=':', label='dft user')
plt.xlabel('k')
plt.ylabel('c_k')
plt.legend()
plt.show()



