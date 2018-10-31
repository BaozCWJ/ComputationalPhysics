import numpy as np
import matplotlib.pyplot as plt
#均匀分割二阶插值方法,num是间隔数,f是源
def FinE(min,max,f,num):
    t=np.linspace(0,max-min,num+1);n=len(t)
    h=t[1]-t[0]
    u=np.zeros(n)
    x=np.zeros(n)
    b=np.zeros(n)
    a=np.zeros(n)
    if n - 1 > 0:
        c = np.zeros(n - 1);
        c[1] = -1/2
    else:
        c = np.zeros(1)
    for k in range(1,n-1):
        b[k]=f(t[k],h)*h*h
        for k in range(1,n-1):
            a[k]=2+c[k-1]
            c[k]=-1/a[k]
    for k in range(1,n):
        if a[k]!=0:
            x[k]=(b[k]+x[k-1])/a[k]
    u[n-1]=x[n-1]
    for k in reversed(range(0,n-1)):
        u[k]=x[k]-c[k]*u[k+1]
    print(b)
    return t,u
#delta函数的数值形式
def delta(x,h):
    if abs(x-0.4)<h/2:
        return -1/h
    else:
        return 0
#精确解
def ExaSol(x):
    s=np.zeros(len(x))
    for j in range(0, len(x)):
        if x[j]<0.4:
            s[j]=-0.6*x[j]
        else:
            s[j]=0.4*(x[j]-1)
    return s

t=np.linspace(0,1,101)
M=ExaSol(t)
x,y=FinE(0,1,delta,100)
plt.figure(figsize=(6,6))
plt.xlim((-0.01,1.01))
plt.ylim((-0.3,0.01))
plt.scatter(x,y,s=20,marker=".",color="blue")
plt.plot(t,M,color="red")
label = ["Exact solution","Numerical point"]
plt.legend(label, loc ='lower center')
plt.grid(True)
plt.show()
