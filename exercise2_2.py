#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 10:10:16 2022

@author: ilariacaporali
"""
#problem: the log-log plot seems to be impossible to generate in this case, I don't know where is the problem

import numpy as np
import matplotlib.pyplot as plt
from numpy.random import random, seed

seed(17)

smin = 1.
smax = 1000.
N = int(1e6)

c = 1/(np.log(smax) -np.log(smin) )

x = random(N)

s = np.exp(x/c)

x_line = np.linspace(smin, smax, 1000)
y_line = c/x_line
plt.hist(s, bins=200, density=True, histtype='step', label='hist')
plt.plot(x_line, y_line, label='$y \propto 1/x$')
plt.xlabel('s')
plt.ylabel('PDF')
plt.legend()
plt.show()

