import numpy as np
num=10                    #调节Hilbert矩阵的尺寸
H=np.zeros((num,num))
A=np.zeros((num,num))
b=np.ones(num)
x=np.zeros(num)
#生成Hilbert矩阵
for i in range(0,num):
    for j in range(0,num):
        H[i,j]=1/(i+j+1)
print(H)
#Cholesky分解
A[0,0]=np.sqrt(H[0,0])
for i in range(1,num):
    temp = 0
    for j in range(0,i):
        if A[j,j]!=0:
             A[i,j]=H[i,j]/A[j,j]
             for k in range(0,j):
                 A[i,j]=A[i,j]-A[j,k]/A[j,j]*A[i,k]
    for j in range(0,i):
        temp=temp-A[i,j]*A[i,j]
    A[i,i]=np.sqrt(H[i,i]+temp)
print(A)
#回带消元
for i in range(0,num):
    if A[i,i]!=0:
        x[i] = b[i] / A[i, i]
        for j in range(0,i):
            x[i]=x[i]-A[i,j]/A[i,i]*x[j]
for i in reversed(range(0,num)):
    if A.T[i,i]!=0:
        b[i] = x[i] / A.T[i, i]
        for j in reversed(range(i+1,num)):
            b[i]=b[i]-A.T[i,j]/A.T[i,i]*b[j]
print(b)




