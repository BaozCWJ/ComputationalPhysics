import numpy as np

def GivQR(B):
    m=len(B)
    Q = np.identity(m)
    R=np.copy(B)
    for i in range(0,m):
        for j in range(i+1,m):
            if R[i,i]!=0:
                t=R[j, i] / R[i, i]
                c=1/np.sqrt(1+t*t)
                x=np.copy(R[i,i:m]);y=np.copy(R[j,i:m])
                R[i,i:m]=c*x+t*c*y
                R[j,i:m]=-t*c*x+c*y
                x = np.copy(Q[:,i]);y = np.copy(Q[:,j])
                Q[:,i]=c*x+t*c*y
                Q[:,j]=-t*c*x+c*y
    return Q,R