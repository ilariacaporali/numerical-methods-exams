#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 12:08:06 2022

@author: ilariacaporali
"""

import numpy as np

l0 = np.array([ 7., 5.,  -5., 10., 2., 1.])
l1 = np.array([ 1., 1.,  -2.,  4., 3., 0.])
l2 = np.array([ 1., 1., 12.,  4., 3., -9.])
l3 = np.array([ 1., -3., - 3., 15., 1., 1.])
l4 = np.array([ 1., -2.,  3.,  4., 5., 6.])
l5 = np.array([ 1., -1.,  1.,  -2., 3., 9.])

A = np.array([l0, l1, l2, l3, l4, l5 ])

b = np.array([ 7., -1., 4., 4., 12., -2.])

x = np.linalg.solve(A, b)

print(x)

xguess = np.ones(len(b), float)

xsol = np.zeros(len(b), float)

tol = 1e-7

while(np.linalg.norm(xguess-xsol)>tol):
    for i in range(len(b)):
        xguess[i] = xsol[i]
        summ=0
        for j in range(len(b)):
            if(j!=i):
                summ += A[i,j]*x[j]
        xsol[i] = (b[i] - summ) / A[i,i]
        
print(xsol)
