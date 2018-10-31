import numpy as np
import math
import matplotlib.pyplot as plt
num=21
x=np.linspace(-1,1,num)
y=np.zeros(num)
N=np.zeros(num)
#Runge函数
for i in range(0,num):
    y[i]=1/(1+25*x[i]*x[i])
#自然三次样条插值
def solveM(x,y):
    h = np.zeros(num)
    b = np.zeros(num)
    L = np.zeros((num, num))
    U = np.zeros((num, num))
    M = np.zeros(num)
    v = np.zeros(num)
    for i in range(0,num-1):
        h[i]=x[i+1]-x[i]
        b[i]=(y[i+1]-y[i])/h[i]*6
    U[1,1]=2*(h[1]+h[0])
#分解插值矩阵
    for i in range(1,num-1):
        L[i,i]=1
        v[i] = b[i] - b[i - 1]
        if i!=num-2:
            L[i+1,i]=h[i]/U[i,i]
            U[i+1,i+1]=2*(h[i+1]+h[i])-h[i]/U[i,i]*h[i]
            U[i,i+1]=h[i]
#回带求解插值系数
    for i in range(1,num-1):
        b[i]=v[i]
        b[i]=b[i]-L[i,i-1]*b[i-1]
    for i in reversed(range(1,num-1)):
        if U[i,i]!=0:
            M[i]=b[i]/U[i,i]
            M[i]=M[i]-U[i,i+1]/U[i,i]*M[i+1]
    return M
#计算分段插值函数
def s(index, t, x, y,Z):
    A=(y[index+1]-y[index])/(x[index+1]-x[index])-(x[index+1]-x[index])*(Z[index+1]-Z[index])/6
    B=y[index]-Z[index]*(x[index+1]-x[index])*(x[index+1]-x[index])/6
    S=A*(t-x[index])+B+Z[index]/(x[index+1]-x[index])*pow(x[index+1]-t,3)/6+Z[index+1]/(x[index+1]-x[index])*pow(t-x[index],3)/6
    return S
#取点画图
N=solveM(x,y)
t=np.linspace(-1,1,51)
P=np.zeros(len(t))
Y=np.zeros(len(t))
for i in range(0,num-1):
    for k in range(math.ceil(len(t) / (len(x) - 1) * i), math.ceil(len(t) / (len(x) - 1) * (i + 1))):
        P[k]=s(i,t[k],x,y, N)
for i in range(0,len(t)):
    Y[i] =1/(1+25*t[i]*t[i])

plt.figure(figsize=(6,6))
plt.xlim((-1,1))
plt.ylim((-1,2))
plt.plot(t,Y,marker="*",color="red")
plt.plot(t,P,marker="+",color="blue")
plt.plot(t,P-Y,marker="o",color="green")
label = ["Standard Curve", "Spline3 curve","Error curve"]
plt.legend(label, loc ='lower center')
plt.grid(True)
plt.show()