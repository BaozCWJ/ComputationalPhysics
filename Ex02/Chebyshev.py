import numpy as np
import math
import matplotlib.pyplot as plt
num=21
x=np.zeros(num)
y=np.zeros(num)
c=np.zeros(num)
T=np.zeros(num)
for i in range(0,num):
    x[i]=np.cos(math.pi*(i+0.5)/num)
    y[i]=1/(1+25*x[i]*x[i])
for i in range(0,num):
    for j in range(0,num):
        c[i]=c[i]+y[j]*np.cos(math.pi*i*(j+0.5)/num)
c=c/num*2
#Chebyshev递推和拟合
def s(n,t,c):
    T[0]=1;T[1]=t;S=-c[0]/2
    for i in range(0,n):
        S=S+T[i]*c[i]
        if i+1!=n and i>0:
            T[i+1]=2*t*T[i]-T[i-1]
    return S
#取点画图
t=np.zeros(2*num-1)
P=np.zeros(len(t))
Y=np.zeros(len(t))
for i in range(0,len(x)-1):
    t[2*i]=x[i]
    t[2*i+1]=(x[i]+x[i+1])/2
t[2*num-2]=x[num-1]
for i in range(0,len(t)):
    Y[i]=1/(1+25*t[i]*t[i])
    P[i]=s(num,t[i],c)

plt.figure(figsize=(6,6))
plt.xlim((-1,1))
plt.ylim((-1,2))
plt.plot(t,Y,marker="*",color="red")
plt.plot(t,P,marker="+",color="blue")
plt.plot(t,P-Y,marker="o",color="green")
label = ["Standard Curve", "Chebyshev curve","Error curve"]
plt.legend(label, loc ='lower center')
plt.grid(True)
plt.show()