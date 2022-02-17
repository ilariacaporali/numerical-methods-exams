#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 26 17:14:31 2022

@author: ilariacaporali
"""

import numpy as np
import matplotlib.pyplot as plt

m, r = np.genfromtxt('exoplanet.eu_catalog.csv', dtype=float, delimiter=',', skip_header=1, usecols=(2,8), unpack=True )

plt.scatter(m, r,label='exoplanet', marker='h', color='green' )
plt.xlabel('$M \; [M_{jupiter}]$')
plt.xlabel('$R \; [R_{jupiter}]$')
plt.legend()
plt.show()

print(len(m))

M=[]
R=[]

for i in range(len(m)):
    if((np.isfinite(m[i])==True) and (np.isfinite(r[i])==True)):
        M.append(m[i])
        R.append(r[i])
        
M = np.array(M)
R = np.array(R)
print(len(M))
print(len(R))