#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 26 15:54:43 2022

@author: ilariacaporali
"""

import numpy as np
import matplotlib.pyplot as plt
from astropy import constants as const

G=1.18482e-4 

m = np.genfromtxt('five_bodies.txt', dtype=float, usecols=(6), unpack=True)
x0 = np.genfromtxt('five_bodies.txt', dtype=float, usecols=(0,1,2), unpack=True)
v0 = np.genfromtxt('five_bodies.txt', dtype=float, usecols=(3,4,5), unpack=True)

tmin = 0
tmax = 3
h = 1e-2
N = int(tmax/h)

x = np.zeros((N,3,5), float)
v = np.zeros((N,3,5), float)
a = np.zeros((N,3,5), float)

x[0,:,:] = x0
v[0,:, :] = v0

for n in range(N-1):
    
    for i in range(5):
        for j in range(5):
            if (j!=i):
                a[n,:,i] += -m[j]* ( x[n,:,i] - x[n,:,j] ) / (np.linalg.norm(x[n,:,i] - x[n,:,j]))**3

    a[n,:,:] = G*a[n,:,:]
    
    x[n+1,:,:] = x[n,:,:] + h*v[n,:,:] + 0.5*h*h*a[n,:,:]
    
    for i in range(5):
        for j in range(5):
            if (j!=i):
                a[n+1,:,i] += - m[j]* ( x[n+1,:,i] - x[n+1,:,j] ) / (np.linalg.norm(x[n+1,:,i] - x[n+1,:,j]))**3

    a[n+1,:,:] = G*a[n+1,:,:]
    
    v[n+1,:,:] = v[n,:,:] + 0.5*h*( a[n,:,:] + a[n+1,:,:] )    

cm = np.zeros((N,3), float)

for i in range(5):
    cm[:,:] += (m[0]*x[:,:,0] + m[1]*x[:,:,1] + m[2]*x[:,:,2] + m[3]*x[:,:,3] + m[4]*x[:,:,4])/sum(m)
    #cm[:,:] += m[i]*x[:,:,i]/sum(m)
    
print(cm)

for i in range(5):
    x[:,:,i] = x[:,:,i] - cm   
    
fig, ax = plt.subplots()
    
for i in range(5):
    stringg='body ' + str(i+1)
    ax.plot(x[:,0,i], x[:,1,i], label=stringg)
    
ax.legend()    
fig.show()

E = np.zeros(N, float)
K = np.zeros(N, float)
U = np.zeros(N, float)

for n in range(N):
    for i in range(5):
        K[n] += 0.5*m[i]*np.linalg.norm(v[n,:,i])**2
        for j in range(5):
            if(j>i):
                U[n] += -m[i]*m[j]*np.linalg.norm(x[n,:,i]-x[n,:,j])
                
U = G*U
E = K + U

L = np.zeros((N,3), float)
Lmod = np.zeros(N, float) 



for n in range(N):
    for i in range(5):
        L[n,:] += m[i]*np.cross(x[n,:,i],v[n,:,i] )
    Lmod[n] = np.linalg.norm(L[n,:])

 
fig2, ax2 = plt.subplots()

ax2.plot(Lmod, label='angular momentum')
ax2.plot(E, label='energy')
ax2.set_xlabel('t')
ax2.set_ylabel('E/L')
ax2.legend()
fig2.show()

        







