import numpy as np
num=10                       #调节Hilbert矩阵的尺寸
H=np.zeros((num,num+1))
x=np.zeros(num)
#生成Hilbert增广矩阵
for i in range(0,num):
    H[i, num] = 1
    for j in range(0,num):
        H[i,j]=1/(i+j+1)
print(H)
#高斯消元算法
for j in range(0, num-1):
    m=j
    for i in range(j+1,num):
        # 支点遴选
        for k in range(j,num):
            if(abs(H[k,j])>abs(H[m,j])):
                m=k
        H[[j,m],:]=H[[m,j],:]
        H[i,]=H[i,]-H[i,j]/H[j,j]*H[j,]
for i in reversed(range(0,num)):
    if H[i,i]!=0:
        x[i] = H[i, num] / H[i, i]
        for j in reversed(range(i+1,num)):
            x[i]=x[i]-H[i,j]/H[i,i]*x[j]
print(x)