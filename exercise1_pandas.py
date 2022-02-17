#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 30 09:30:15 2022

@author: ilariacaporali
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import pandas as pd

data = pd.read_csv('SEVN_output.csv')

data = data.dropna(subset=['Mass_0', 'Mass_1'])

m1 = data['Mass_0']
m2 = data['Mass_1']

print(len(m1))
print(len(m2))

'''
plt.scatter(m1, m2, label='data', marker='*')
plt.xlabel('$M_1 \; [M_{\odot}]$')
plt.ylabel('$M_2 \; [M_{\odot}]$')
plt.show()
'''

plt.hist2d(m1, m2, bins=50, norm= colors.LogNorm())
plt.xlabel('$M_1 \; [M_{\odot}]$')
plt.ylabel('$M_2 \; [M_{\odot}]$')
cbar = plt.colorbar()
cbar.set_label('# of systems with a given combination of m1, m2')
plt.show()

type1 = data['RemnantType_0']
type2 = data['RemnantType_1']

type1.astype(int)
type2.astype(int)

a = np.where((type1==6) & (type2==6))

print(len(a[0]))