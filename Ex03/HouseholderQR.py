import numpy as np
#矩阵的HouseholderQR分解
def HouQR(B):
    m=len(B);
    Q = np.identity(m)
    R=np.copy(B)
    for i in range(0,m):
        x = np.zeros(m)
        x[i:m]=R[i:m,i]
        x[i]=x[i]-np.sqrt(np.dot(x,x))
        temp=np.dot(x,x)
        if temp != 0:
            for j in range(0, m):
                Q[j,i:m] = Q[j,i:m] - 2 * x[i:m] * np.dot(Q[j,i:m], x[i:m]) / temp
            for j in range(i, m):
                R[i:m, j] = R[i:m, j] - 2 * x[i:m] * np.dot(R[i:m, j], x[i:m]) / temp
    return Q,R

#标准QR分解
def StandQR(B,k):
    m=len(B)
    Q=np.identity(m)
    Qbar=Q;R=B
    for i in range(0,k):
        Q,R=HouQR(R.dot(Q))
        Qbar=Q.dot(Qbar)
    return R.dot(Q)
#Hessenberg约化
def Hessenberg(B):
    m = len(B);n=len(B[0])
    H = B
    for i in range(0, n-1):
        P = np.zeros((m, m))
        x = np.zeros(m)
        for j in range(i+1, m):
            x[j] = H[j, i]
        x[i+1] = x[i+1]-np.sqrt(np.dot(x.T, x))
        temp=np.dot(x.T, x)
        if temp!= 0:
            P=np.identity(m)-2*np.tensordot(x,x,0)/temp
            H = np.dot(P.T, H).dot(P)
    return H

