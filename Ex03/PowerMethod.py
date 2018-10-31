import numpy as np
#为了方便起见，写个kronecker delta函数
def delta(i,j):
    if i==j: s=1
    else: s=0
    return s
#生成周期条件的链矩阵并输出，num决定矩阵尺寸
def ChainMatrix(num):
    A=np.zeros((num,num))
    for i in range(0,num):
        for j in range(0,num):
            A[i,j]=2*delta(i,j)-delta(i+1,j)-delta(i-1,j)
    A[0,num-1]=-1;A[num-1,0]=-1
    return A
print(ChainMatrix(10))
#幂次法求解链矩阵的最大本征值和相应本征矢，k是迭代次数
def Pow(A,k):
    m=len(A)
    q=np.zeros(m);q[0]=1
    for i in range(0,k):
        z=A.dot(q)
        q=z/np.sqrt(z.T.dot(z))
        v=q.T.dot(A.dot(q))
    return v,q
print(Pow(ChainMatrix(10),1000))