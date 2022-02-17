#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 12:30:08 2022

@author: ilariacaporali
"""

import numpy as np
import matplotlib.pyplot as plt

tmin = 0
tmax = 5
h = 0.01
N = int(tmax/h)

m = np.array([6., 2.])

x10 = np.array([0.,0., 0.]) 
x20 = np.array([0.,2., 0.]) 
x0 = np.array([x10, x20])

x = np.zeros((N, 2, 3), float)
x[0,:,:] = x0

v10 = np.array([0.,0., 0.]) 
v20 = np.array([2.,0., 0.]) 
v0 = np.array([v10, v20])

v = np.zeros((N, 2, 3), float)
v[0,:,:] = v0

a = np.zeros((N, 2, 3), float)

for n in range(N-1):
    
    for i in range(2):
        for j in range(2):
            if(j!=i):
                a[n,i,:] = -m[j]*(x[n,i,:]-x[n,j,:])/np.linalg.norm(x[n,i,:]-x[n,j,:])**3
    
    x[n+1,:,:] = x[n,:,:] + h*v[n,:,:] + 0.5*h*h*a[n,:,:]
    
    for i in range(2):
        for j in range(2):
            if(j!=i):
                a[n+1,i,:] = -m[j]*(x[n+1,i,:]-x[n+1,j,:])/np.linalg.norm(x[n+1,i,:]-x[n+1,j,:])**3
                
    v[n+1,:,:] = v[n,:,:] + 0.5*h*( a[n,:,:] + a[n+1,:,:] )
    
xcm = np.zeros((N,3), float)
xc = np.zeros((N, 2, 3), float)

for i in range(2):
    xcm[:,:] += m[i]*x[:,i,:]/sum(m)
    
xc[:,0,:] = x[:,0,:] - xcm
xc[:,1,:] = x[:,1,:] - xcm
'''  
plt.plot(xc[:,0,0], xc[:,0,1], label='body 1', color='green')
plt.plot(xc[:,1,0], xc[:,1,1], label='body 2', color='purple')
plt.legend()
plt.show()
'''
K = np.zeros(N, float)
U = np.zeros(N, float)
E = np.zeros(N, float)

for n in range(N):
    for i in range(2):
        K[n] += 0.5*m[i]*np.linalg.norm(v[n,i,:])**2
        for j in range(2):
            if(j!=i):
                U[n] += -m[i]*m[j]/np.linalg.norm(x[n,i,:]-x[n,j,:])
                
E = U + K

E = abs((E - E[0])/E[0])
'''
plt.plot(E, label='energy')
plt.xlabel('time')
plt.ylabel('Energy')
plt.legend()
plt.show()
'''
L = np.zeros(N, float)

for n in range(N):#time
    for k in range(2):#body
        L[n] += m[k]* np.linalg.norm(v[n,k,0]*x[n,k,1] - v[n,k,1]*x[n,k,0])
        
L = abs((L - L[0])/L[0])
                    
plt.plot(L, label='angular momentum')
plt.xlabel('time')
plt.ylabel('Angular momentum')
plt.legend()
plt.show()
            
            


            

                
