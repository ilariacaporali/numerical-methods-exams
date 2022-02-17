#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 11:14:47 2022

@author: ilariacaporali
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors

m1_raw, m1_type_raw, m2_raw, m2_type_raw = np.genfromtxt('SEVN_output.csv', delimiter=',', dtype=float, usecols=(2,7,9,14), skip_header=1, unpack=True)

m1 = []
m2 = []
m1_type=[]
m2_type=[]

for i in range(len(m1_raw)):
    if (np.isfinite(m1_raw[i])==True and np.isfinite(m2_raw[i])==True):
        m1.append(m1_raw[i])
        m2.append(m2_raw[i])
        m1_type.append(m1_type_raw[i])
        m2_type.append(m2_type_raw[i])
        
m1 = np.array(m1)
m2 = np.array(m2)
m1_type = np.array(m1_type)
m2_type = np.array(m2_type)
        
print('# of BSs: ', len(m1))

'''
plt.scatter(m1, m2, label='BSs', marker='*', color='black')
plt.xlabel('$M_1 \; [M_{\odot}]$')
plt.ylabel('$M_2 \; [M_{\odot}]$')
plt.legend()
plt.show()
'''

plt.hist2d(m1, m2, bins=50, norm=colors.LogNorm())
plt.xlabel('$M_1 \; [M_{\odot}]$')
plt.ylabel('$M_2 \; [M_{\odot}]$')
cbar = plt.colorbar()
cbar.set_label('#BSs')
plt.show()

m1_BH = []
m2_BH = []

for i in range(len(m1)):
    if (m1_type[i] == 6 and m2_type[i] == 6):
        m1_BH.append(m1_type[i])
        m2_BH.append(m2_type[i])
        
m1_BH = np.array(m1_BH)
m2_BH = np.array(m2_BH)
print('# BSs with both BH remnants : ', len(m1_BH))






