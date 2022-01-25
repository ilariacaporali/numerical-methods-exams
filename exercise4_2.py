#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 11:01:12 2022

@author: ilariacaporali
"""

import numpy as np
import matplotlib.pyplot as plt

#main

m = np.array([3, 4, 5])

x10 = np.array([0., 4., 0.])
x20 = np.array([-3., 0., 0.])
x30 = np.array([0., 0., 0.])

h = 1e-5
tmin = 0
tmax = 5
N = int(tmax/h)

x1 = np.zeros((N,3), float)
x2 = np.zeros((N,3), float)
x3 = np.zeros((N,3), float)

x1[0,:] = x10
x2[0,:] = x20
x3[0,:] = x30

x = np.array([x1,x2,x3])

zz = np.zeros((N,3), float)

v = np.array([zz,zz,zz])

a = np.array([zz,zz,zz])

a_mid = np.array([zz,zz,zz])

x_mid = np.array([zz,zz,zz])

k1x = np.array([zz,zz,zz])

k1v = np.array([zz,zz,zz])

k2x = np.array([zz,zz,zz])

k2v = np.array([zz,zz,zz])

for i in range(N-1):
    
    for k in range(3):
        for j in range(3):
            if (j!=k):
                a[k,i,:] += -m[j] * (x[k,i,:]-x[j,i,:]) / (np.linalg.norm(x[k,i,:]-x[j,i,:]) )**3
                
    k1x[:,i,:] = 0.5 * h * v[:,i,:]
    k1v[:,i,:] = 0.5 * h * a[:,i,:]
    x_mid[:,i,:] = x[:,i,:] + k1x[:,i,:]
    
    for k in range(3):
        for j in range(3):
            if (j!=k):
                a_mid[k,i,:] += -m[j] * (x_mid[k,i,:]-x_mid[j,i,:]) / (np.linalg.norm(x_mid[k,i,:]-x_mid[j,i,:]) )**3
                
    
    k2x[:,i,:] = h * ( v[:,i,:] +k1v[:,i,:] )
    k2v[:,i,:] = h *a_mid[:,i,:]
    x[:,i+1,:] = x[:,i,:] + k2x[:,i,:]
    v[:,i+1,:] =v[:,i,:] + k2v[:,i,:]

'''    
plt.plot(x[0,:,0], x[0,:,1], label='body 1')
plt.plot(x[1,:,0], x[1,:,1], label='body 2')
plt.plot(x[2,:,0], x[2,:,1], label='body 3')
plt.show()
'''
K = np.zeros(N, float)
U = np.zeros(N, float)
E = np.zeros(N, float)


for i in range(N):
    
    for k in range(3):
        K[i] += 0.5*m[k]*np.linalg.norm(v[k,i,:])**2
        
        for j in range(3):
            if(j>k):
                U[i] += -m[k]*m[j]/np.linalg.norm(x[j,i,:]- x[k,i,:])

E = K + U 
                
dE = np.zeros(N-1, float)

for i in range(N-1):
    dE[i] = (E[i+1] - E[i])/(E[i])
    
t = np.linspace(tmin, tmax, N-1)

plt.plot(t, dE, label='energy')
plt.xlabel('t')
plt.ylabel('$ |(E - E_{old})/E_{old} | $')
        
    
        




    

