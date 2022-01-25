#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 09:55:40 2022

@author: ilariacaporali
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors


M1, M2 = np.genfromtxt('data_BBHs_0.0002.txt', dtype='float', skip_header=1, usecols=(3, 4), unpack= True)

'''
plt.scatter(M2, M1, marker='*', color='black', label='BBH')
plt.xlabel('$M_2 \; \; [M_{\odot} ]$')
plt.ylabel('$M_1 \; \; [M_{\odot} ]$')
plt.legend()
plt.show()
'''
plt.hist2d(M2, M1, bins=50, norm=colors.LogNorm() )
plt.xlabel('$M_2 \; \; [M_{\odot} ]$')
plt.ylabel('$M_1 \; \; [M_{\odot} ]$')
cbar = plt.colorbar()
cbar.set_label('# BBHs per cell')
plt.show()

M1_mean = np.mean(M1)
M2_mean = np.mean(M2)
M1_std = np.std(M1)
M2_std = np.std(M2)

print('M1 : mean = ', M1_mean, ', std = ', M1_std )
print('M2 : mean = ', M2_mean, ', std = ', M2_std )

