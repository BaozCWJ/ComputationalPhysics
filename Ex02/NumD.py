import numpy as np
import math

#被积函数
def f(p,x):
    S=math.pi*pow(p,-2)*(np.exp(p*p*x)*(1+6/np.sqrt(math.pi)*np.exp(-math.pi/p*math.pi/p))-1)
    return S
#Simpson积分(考虑边界修正)
def Simp(n,x):
    InF = x*math.pi/n/3+2*f(1/n,x)/n/3
    for i in range(1,n):
        if i%2==0:
            InF=InF+(f(i/n,x)+2*f((i+1)/n,x))/n/3
        if i%2==1:
            InF=InF+(2*f(i/n,x)+f((i+1)/n,x))/n/3
    return InF
#搜寻n的种类
def SearchN(n):
    s=0
    for i in range(-math.ceil(np.sqrt(n)),math.ceil(np.sqrt(n))+1):
        for j in range(-math.ceil(np.sqrt(n)), math.ceil(np.sqrt(n))+1):
            for k in range(-math.ceil(np.sqrt(n)), math.ceil(np.sqrt(n))+1):
                if n==i*i+j*j+k*k:
                    s=s+1
    return s
#求和项
def Sum(x,n):
    Y=-1/(x)
    for i in range(1,n+1):
        Y=Y+SearchN(i)/(i-x)*np.exp(-i)
    Y=Y*np.exp(x)/2/pow(math.pi,1/2)
    return Y
#二分法求解，e是精度，num是数值积分的段数
def Z(x,num):
    S=Sum(x, 27) + Simp(num, x) - pow(math.pi, 3 / 2) - math.pi - x / 4 * pow(math.pi, 3 / 2)
    return S
def Bisec(e,num):
    temp1=0.2;temp2=0.9
    y1 = Z(temp1,num)
    y2 = Z(temp2,num)
    if y1*y2<0:
        while(abs(temp1-temp2)>e):
            r=temp1*0.5+temp2*0.5
            y=Z(r,num)
            if y*y1<0:
                temp2=r;y2=y
            if y*y2<0:
                temp1=r;y1=y
        return r
    else:
        return 0

#输出方程的解(精度为1e-6，积分间隔为50等分)
print(Bisec(1e-6,50))







