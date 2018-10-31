import numpy as np
import math
import matplotlib.pyplot as plt
num=9
t=np.linspace(0,8,num)
x=np.zeros(num)
y=np.zeros(num)
Mx=np.zeros(num)
My=np.zeros(num)

#Cardioid曲线
for i in range(0,num):
    t[i]=2*math.pi*i/(num-1)
    y[i]=np.sin(t[i])*(1-np.cos(t[i]))
    x[i]=np.cos(t[i])*(1-np.cos(t[i]))
#自然三次样条插值
def solveM(x,y):
    M=np.zeros(num)
    h = np.zeros(num)
    b = np.zeros(num)
    L = np.zeros((num, num))
    U = np.zeros((num, num))
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

def s(index, r, x, y,Z):
    A=(Z[index+1]-Z[index])/(x[index+1]-x[index])/6
    B=Z[index]/2
    C=(y[index+1]-y[index])/(x[index+1]-x[index])-(Z[index+1]+2*Z[index])*(x[index+1]-x[index])/6
    S=y[index]+(r-x[index])*(C+(r-x[index])*(B+(r-x[index])*A))
    return S
#取点画图
Mx=solveM(t,x)
My=solveM(t,y)
tt=np.zeros(91)
Px=np.zeros(len(tt))
Py=np.zeros(len(tt))
Y=np.zeros(len(tt))
X=np.zeros(len(tt))
for i in range(0,len(tt)):
    tt[i]=2*math.pi*i/(len(tt)-1)
    Y[i]=np.sin(tt[i])*(1-np.cos(tt[i]))
    X[i]=np.cos(tt[i])*(1-np.cos(tt[i]))
for i in range(0,num-1):
    for k in range(math.ceil(len(tt) / (len(t) - 1) * i), math.ceil(len(tt) / (len(t) - 1) * (i + 1))):
        Px[k]=s(i,tt[k],t,x, Mx)
        Py[k] = s(i, tt[k], t, y, My)
plt.figure(figsize=(6,6))
plt.xlim((-3,1))
plt.ylim((-2,2))
plt.plot(x,y,'ro',color="green")
plt.plot(X,Y,color="red")
plt.plot(Px,Py,color="blue")
label = ["Sample Point","Standard Curve", "Spline3 curve"]
plt.legend(label, loc ='lower center')
plt.grid(True)
plt.show()