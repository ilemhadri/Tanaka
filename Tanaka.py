# -*- coding: utf-8 -*-
"""
Created on Fri May 19 16:04:28 2017

@author: thinkpad
"""

import numpy as np
import matplotlib.pyplot as plt 
def sign(x):
    return 2*(x>=0)-1
    
N=10000
m=10

Res=[]
for i in range(m):
    dW = np.random.normal(0,1,N+1)/np.sqrt(N)
    #starting from 0    
    #dW[0]=0
    W = np.cumsum(dW)
    Res.append(np.cumsum(sign(W)*dW))
Res=np.array(Res)
Res = np.mean(Res,axis=0)
X=np.arange(N+1)/N
plt.plot(X,Res)
plt.plot(X,2*np.sqrt(X*2/np.pi))
plt.show()