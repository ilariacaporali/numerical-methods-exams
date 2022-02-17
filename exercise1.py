#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 26 09:25:07 2022

@author: ilariacaporali
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors

M, R = np.genfromtxt('BBH_EAGLE25Mpc_z01.txt', dtype='float', skip_header=1, usecols=(0,1), unpack=True)


'''
plt.scatter(M, R, marker='*', color='black')
plt.xscale('log')
plt.yscale('log')
plt.xlabel('$ M \;  [M_{\odot}] $')
plt.ylabel('$ R_{BBH} \; [Gyr^{-1]}$')
plt.show()
'''
log_M = np.log10(M)
log_R = np.log10(R)

plt.hist2d(log_M, log_R, bins =50, norm = colors.LogNorm())
plt.xlabel('$ log_{10}(M) \;  [M_{\odot}] $')
plt.ylabel('$ log_{10}(R_{BBH}) \; [Gyr^{-1]}$')
cbar = plt.colorbar()
cbar.set_label(' # systems with a given combination of M, R')
plt.show()

M_median = np.median(M)
R_median = np.median(R)

M_std = np.std(M)
R_std = np.std(R)

print('M : median = ', M_median,' , std = ', M_std, ' Msun ' )
print('R : median = ', R_median,' , std = ', R_std, ' Gyr^-1 ' )