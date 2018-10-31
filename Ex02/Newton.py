import numpy as np
import matplotlib.pyplot as plt

num=21
x=np.linspace(-1,1,num)
y=np.zeros(num)
A=np.zeros((num,num))
a=np.zeros(num)
for i in range(0,num):
    y[i]=1/(1+25*x[i]*x[i])

for i in range(0,num):
    A[i,0]=1
    for j in range(0,i):
            A[i,j+1]=A[i,j]*(x[i]-x[j])
for i in range(0,num):
    if A[i,i]!=0:
        a[i] = y[i] / A[i, i]
        for j in range(0,i):
            a[i]=a[i]-A[i,j]/A[i,i]*a[j]

def f(t,a):
    F=a[num-1]
    for i in reversed(range(0,len(a)-1)):
        F=F*(t-x[i])+a[i]
    return F

t=np.linspace(-1,1,2*num-1)
P=np.zeros(2*num-1)
Y=np.zeros(2*num-1)
for i in range(0,len(t)):
    P[i]=f(t[i],a)
    Y[i] = 1/(1 + 25 * t[i] * t[i])

plt.figure(figsize=(6,6))
plt.xlim((-1,1))
plt.ylim((-1,2))
plt.plot(t,Y,marker="*",color="red")
plt.plot(t,P,marker="+",color="blue")
plt.plot(t,P-Y,marker="o",color="green")
label = ["Standard Curve", "Newton curve","Error curve"]
plt.legend(label, loc ='lower center')
plt.grid(True)
plt.show()
