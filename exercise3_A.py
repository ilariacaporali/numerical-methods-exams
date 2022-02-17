#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 10:27:25 2022

@author: ilariacaporali
"""

import numpy as np

l0 = np.array( [0., 5., 15., 0., 1. ] )
l1 = np.array( [1., 0., 2., 13., 9. ] )
l2 = np.array( [17., 5., 17., 2., 1. ] )
l3 = np.array( [1., 12., 4., 13., 9. ] )
l4 = np.array( [1., 2., 4., 13., 0. ] )

A = np.array( [l0, l1, l2, l3,l4] )

b = np.array( [17., 27., 17., 1., 12. ] )

x = np.linalg.solve(A, b)
print(x)