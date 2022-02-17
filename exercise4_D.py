#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 11:20:41 2022

@author: ilariacaporali
"""

import numpy as np
import matplotlib.pyplot as plt

m = np.array([3., 1.])
x10 = np.array([0., 0.])
x20 = np.array([1., 0.])
x0 = np.array([x10, x20])
v10 = np.array([0., 0.])
v20 = np.array([0., 2.])
v0 = np.array([v10, v20])

tmin = 0
tmax =5
h=0.001
b = 0.1
N = int(tmax/h)

x = np.zeros((N, 2, 2), float)
x[0,:,:] = x0

v = np.zeros((N, 2, 2), float)
v[0,:,:] = v0

a = np.zeros((N, 2, 2), float)

for i in range(N-1):
    
    for k in range(2):
        for j in range(2):
            if(j!=k):
                a[i,k,:] = -m[j] * (x[i,k,:] - x[i,j,:])/ ( np.linalg.norm((x[i,k,:] - x[i,j,:]))**3 ) - b*v[i,k,:]
    
    x[i+1,:,:] = x[i,:,:] + v[i,:,:]*h
    v[i+1,:,:] = v[i,:,:] + a[i,:,:]*h
    
cm = np.zeros( (N, 2), float )

cm[:,:] = (m[0]*x[:,0,:] + m[1]*x[:,1,:] )/ (sum(m) )

x1_cmrf = x[:,0,:] - cm[:,:]
x2_cmrf = x[:,1,:] - cm[:,:]
    
#plt.plot(x[:,0,0], x[:,0,1], color='green', label='body 1')
#plt.plot(x[:,1,0], x[:,1,1], color='purple', label='body 2')
plt.plot(x1_cmrf[:,0], x1_cmrf[:,1], color='green', label='body1' )
plt.plot(x2_cmrf[:,0], x2_cmrf[:,1], color='violet', label='body2' )
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()

K = np.zeros(N, float)
U = np.zeros(N, float)
E = np.zeros(N, float)

for n in range(N):
    for i in range(2):
        K[n] += 0.5*m[i]*np.linalg.norm(v[n,i,:])**2
        for j in range(2):
            if(j>i):
                U[n] += -m[i]*m[j]/(np.linalg.norm( x[n,i,:] -x[n,j,:] ))
'''  
#binary system energy in the cm rf
for n in range(N):
    K[n] = ( 0.5*m[0]*m[1]*np.linalg.norm(v[n,0,:]- v[n,1, :] )**2 ) / (m[0] + m[1])
    U[n] =-m[0]*m[1]/ np.linalg.norm( x[n,0,:] -x[n,1,:] )
              
E = K + U
dE = np.zeros(N, float)

for n in range(N):
    dE[n] = (E[n] - E[0])/(E[0])
    
t = np.linspace(tmin, tmax, len(dE))

plt.plot(t, dE, color='darkcyan', label='energy variation')
plt.xlabel('time')
plt.ylabel('dE')
plt.legend()
plt.show()
'''
            

