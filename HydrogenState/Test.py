from function import *
import matplotlib.pyplot as plt
import numpy as np
'''
#Laguerre Test
for n in [3,10,30]:
    for alpha in [2,20,40]:
        for x in [1e-3,1,1e2]:
            print('n=',n,'alpha=',alpha,'x=',x,Laguerre(alpha=alpha,n=n,x=x))

#SphericalHarmonic Test
for theta in [1/1000,3/10,501/1000]:
    for L in [100,500,1000]:
        for M in [1,L//100,L//10,L-1]:
            print('theta=',theta*math.pi,'l=',L,'m=',M,SphericalHarmonic(L,M,theta*math.pi,math.pi/5))

#311Energy
print('E311=',Energy(fr,0,60,1e-6))
'''
#Density XY picture
n=2
l=1
m=0
rmax=5e-10
N=100
data1=DensityHeatMap(n,l,m,rmax,N)
data2=DensityHeatMap(n,l,m-1,rmax,N)
data3=DensityHeatMap(n,l,m+1,rmax,N)
fig = plt.figure()
ax = fig.add_subplot(131)
im = ax.imshow(data1, cmap=plt.cm.winter)
ax = fig.add_subplot(132)
im = ax.imshow(data2, cmap=plt.cm.winter)
ax = fig.add_subplot(133)
im = ax.imshow(data3, cmap=plt.cm.winter)
plt.show()