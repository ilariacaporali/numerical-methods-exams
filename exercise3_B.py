#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 10:08:12 2022

@author: ilariacaporali
"""

import numpy as np
'''
l0 = np.array( [0., 5., 15., 0., 1. ] )
l1 = np.array( [1., 0., 2., 13., 9. ] )
l2 = np.array( [17., 5., 17., 2., 1. ] )
l3 = np.array( [1., 12., 4., 13., 9. ] )
l4 = np.array( [1., 2., 4., 13., 0. ] )
'''
l0 = np.array( [0., 2., 1., 0., -1. ] )
l1 = np.array( [1., 0., 2., 11., 7. ] )
l2 = np.array( [2., 5., 7., 2., 1. ] )
l3 = np.array( [1., 17., -1., 0., 9. ] )
l4 = np.array( [1., 2., 3., 11., 0. ] )

A = np.array( [l0, l1, l2, l3,l4] )

b = np.array( [7., 17., 7., -1., 1. ] )

#x = np.linalg.solve(A, b)
#print(x)

A2 = np.array( [l2, l3, l0, l4, l1 ] )
b2 = np.array( [b[2], b[3], b[0], b[4], b[1]])

xguess = np.ones(len(b2), float)
xsol = np.zeros(len(b2), float)
tol = 1e-7

while(np.linalg.norm(xsol-xguess)>tol):
    
    for i in range(len(xsol)):
        xguess[i] = xsol[i]
        summ = 0
        for j in range(len(xsol)):
            if(j!=i):
                summ += A2[i,j]*xguess[j]
        xsol[i] = ( b2[i] - summ ) / A2[i,i]
        
print(xsol)
        
