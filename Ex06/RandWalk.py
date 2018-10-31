import numpy as np
import math
import matplotlib.pyplot as plt
from numba import jit


@jit
def RandWalk(L,N,T):
    pos=np.zeros(T)
    pos2=np.zeros(T)
    Prob=np.zeros(2*T-1)
    for i in range(N):
        temp=np.zeros(T)
        for j in range(T-1):
            temp[j+1]=temp[j]+2*math.ceil(np.random.random_sample()-L)-1
        x=math.floor(temp[T-1])
        Prob[x+T-1]=Prob[x+T-1]+1
        pos=pos+temp
        pos2=pos2+temp*temp
    return pos/N,pos2/N-pos/N*pos/N,Prob/N
def HeatKernel(L,x,t):
    return 2*np.exp(-(x-(1-2*L)*t)**2/(8*t*(1-L)*L))/np.sqrt(8*math.pi*t*(1-L)*L)
N=100000;T=1001;l=0.25
mu,sig,p=RandWalk(l,N,T)
t=np.linspace(0,T-1,T)
tt=np.linspace(-T+1,T-1,2*T-1)
H=HeatKernel(l,tt,T-1)


plt.figure(1)
plt.xlim((0,T))
plt.ylim((min(mu),max(mu)))
plt.plot(t,mu,linewidth=0.8,color="blue")
label = ["Mean"]
plt.legend(label, loc ='lower center')
plt.grid(True)

plt.figure(2)
plt.xlim((0,T))
plt.ylim((min(sig),max(sig)*1.1))
plt.plot(t,sig,linewidth=0.8,color="blue")
label = ["Variance"]
plt.legend(label, loc ='lower center')

plt.grid(True)
plt.figure(3)
plt.xlim((-T,T))
plt.ylim((min(p),max(p)*1.1))
plt.plot(tt,H,linewidth=0.8,color="blue")
plt.scatter(tt,p,s=0.8,color="red")
label = ["Heat Kernel","RW Distribution"]
plt.legend(label, loc ='upper right')
plt.grid(True)
plt.show()