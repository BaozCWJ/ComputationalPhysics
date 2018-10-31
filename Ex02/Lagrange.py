import numpy as np
import matplotlib.pyplot as plt
num=21
x=np.linspace(-1,1,num)
y=np.zeros(num)

for i in range(0,num):
    y[i]=1/(1+25*x[i]*x[i])
#构造lagrange多项式函数
def l(r,j,a):
    L=1
    for i in range(0,num):
        if i!=j:
            L=L*(r-a[i])/(a[j]-a[i])
    return L
#用Lagrange多项式拟合
def f(r,a,b):
    F=0
    for i in range(0,num):
        F=F+b[i]*l(r,i,a)
    return F
#选点画图
t=np.linspace(-1,1,2*num-1)
P=np.zeros(len(t))
Y=np.zeros(len(t))
for i in range(0,len(t)):
    P[i]=f(t[i],x,y)
    Y[i] =1/(1+25*t[i]*t[i])
plt.figure(figsize=(6,6))
plt.xlim((-1,1))
plt.ylim((-1,2))
plt.plot(t,Y,marker="*",color="red")
plt.plot(t,P,color="blue",marker="+")
label = ["Standard curve", "Lagrange curve"]
plt.legend(label, loc ='lower center')
plt.grid(True)
plt.show()

