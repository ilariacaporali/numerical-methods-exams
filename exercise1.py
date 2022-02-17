#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 09:37:55 2022

@author: ilariacaporali
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors

m1, m2 = np.genfromtxt('BBH_first_gen.txt', dtype = 'float', skip_header=1, usecols=(1,2), unpack=True)
'''
plt.scatter(m2, m1, marker='*', color='black', label='BBH mergers')
plt.xlabel('$M_2 \; \; [M_{\odot}]$')
plt.ylabel('$M_1 \; \; [M_{\odot}]$')
plt.legend()
plt.show()
'''

plt.hist2d(m2, m1, bins=50, norm=colors.LogNorm(), )
cbar=plt.colorbar()
cbar.set_label('#BBH mergers per cell')
plt.xlabel('$M_2 \; \; [M_{\odot}]$')
plt.ylabel('$M_1 \; \; [M_{\odot}]$')
plt.show()

m1_m = np.mean(m1)
m1_std = np.std(m1)
m2_m = np.mean(m2)
m2_std = np.std(m2)

print('M1 : mean = ', m1_m, ' std = ', m1_std)
print('M2 : mean = ', m2_m, ' std = ', m2_std)