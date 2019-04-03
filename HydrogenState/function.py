import numpy as np
import math
from numba import jit

def HugeFactorial(l,m):
    s=1
    for i in range(math.floor(l-m),math.floor(l+m)):
        s=s*(i-l+m+1)/np.sqrt(i+1)
        if i<l:
            s=s/(l-i)
    return s


def Laguerre(alpha,n,x):
    if n==0:
        return 1
    elif n==1:
        return -x+alpha+1
    elif n==2:
        return (x*x-2*(alpha+2)*x+(alpha+1)*(alpha+2))/2
    elif n>=3:
        return (2*n-1+alpha-x)/n*Laguerre(alpha,n-1,x)-(n-1+alpha)*Laguerre(alpha,n-2,x)/n

def Legendre(l,x):
    if l==0:
        return 1
    elif l==1:
        return x
    elif l==2:
        return (3*x*x-1)/2
    elif l>=3:
        a=x
        b=(3*x*x-1)/2
        for i in range(2,l):
            c=(2*i+1)/(i+1)*x*b-(i)/(i+1)*a
            a=b
            b=c
        return c


def AssoLegendre(l,m,x):
    if l==m:
        return pow(-1,m)*(HugeFactorial(l,m)/pow(2,m))*pow(1-x*x,m/2)
    elif l==m+1:
        return x*(2*m+1)*pow(-1,m)*HugeFactorial(l,m)/pow(2,m)*pow(1-x*x,m/2)
    elif l>=m+2:
        a=pow(-1,m)*(HugeFactorial(l,m)/pow(2,m))*pow(1-x*x,m/2)
        b=x*(2*m+1)*a
        for i in range(m+1,l):
            c=x*(2*i+1)/(i+1-m)*b-(i+m)/(i+1-m)*a
            a=b
            b=c
        return c

def SphericalHarmonic(l,m,theta,phi):
    if m!=0:
        return np.sqrt((2 * l + 1)/ (4* math.pi)) * AssoLegendre(l, abs(m),math.cos(theta))*complex(math.cos(m*phi),math.sin(m*phi))
    elif m==0:
        x=math.cos(theta)
        if abs(theta)==math.pi/2:
            x=0
        return np.sqrt((2 * l + 1)/ (4* math.pi)) *Legendre(l,x)


def HydrogenState(n,l,m,r,theta,phi):
    a=5.29e-11
    rho=2*r/(n*a)
    return np.sqrt(pow(2/(n*a),3)*math.factorial(n-l-1)/(2*n)/math.factorial(n+l))*math.exp(-rho/2)*pow(rho,l)*Laguerre(n=n-l-1,alpha=2*l+1,x=rho)*SphericalHarmonic(l,m,theta,phi)

def Density(n,l,m,r,theta,phi):
    return abs(HydrogenState(n,l,m,r,theta,phi))**2


@jit
def DensityHeatMap(n,l,m,rmax,Num):
    data = np.zeros((2 * Num + 1, 2 * Num + 1))
    for i in range(2*Num + 1):
        for j in range(2*Num + 1):
            r = np.sqrt((i-Num)**2 + (j-Num)**2) / Num * rmax
            angle=math.atan2(Num-j,i-Num)
            data[i, j] = pow(Density(n=n, l=l, m=m, r=r, theta=math.pi/2, phi=angle),1/2)
    return data

#n=3,l=1,m=1 Energy

def fr(x):
    f=np.exp(-x/3)*x*(6-x)
    df=np.exp(-x/3)*(6-4*x+x*x/3)
    ddf=np.exp(-x/3)*(-6+2*x-x*x/9)
    S=f*(f*(1-x)-x*df-x*x*ddf/2)
    return 8/pow(3,9)*S

def Trapz(f,a,b,N):
    h=(b-a)/N;S=0
    for i in range(N):
        S=S+(f(a+(i*h))+f(a+(i+1)*h))/2*h
    return S

def Energy(f,a,b,epsilon):
    E=0
    n=1
    while abs(E+1/18)>epsilon:
        E=Trapz(f,a,b,n)
        n=n*2
    return E



