import numpy as np
def RK2(ini,step,iter,f):
    S=np.zeros((iter,len(ini)))
    t=np.zeros(iter)
    S[0,]=ini
    for k in range(iter-1):
        k1=f(t[k],S[k,])
        k2=f(t[k]+step,S[k,]+step*k1)
        S[k+1,]=S[k,]+(k1+k2)*step/2
        t[k+1]=t[k]+step
    return t,u
def RK4(ini,step,iter,f):
    S=np.zeros((iter,len(ini)))
    t=np.zeros(iter)
    S[0,]=ini
    for k in range(iter-1):
        k1=f(t[k],S[k,])
        k2=f(t[k]+step/2,S[k,]+step/2*k1)
        k3=f(t[k]+step/2,S[k,]+step/2*k2)
        k4=f(t[k]+step,S[k,]+step*k3)
        S[k+1,]=S[k,]+(k1+2*k2+2*k3+k4)*step/6
        t[k+1]=t[k]+step
    return S
