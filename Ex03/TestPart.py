import numpy as np
import HouseholderQR
import GivensQR
import time
#从文本读取矩阵M
M=[]
with open('matrix.txt','r') as file_to_read:
    while True:
        row=file_to_read.readline()
        if not row:
            break
            pass
        M_tmp=[float(i) for i in row.split()]
        M.append(M_tmp)
        pass
    M=np.array(M)
print(M)
#检查Householder分解的有效性
Q1,R1=HouseholderQR.HouQR(M)
print(np.dot(Q1,R1))
#检查Givens分解的有效性
Q2,R2=GivensQR.GivQR(M)
print(np.dot(Q2,R2))
#效率测试函数
def Test(m,num,Method):
    time_start = time.time()
    RandomMatrix = [2 * np.random.random(size=(m, m)) - np.ones(m) for i in range (num)]
    for A in RandomMatrix:
        Method(A)
    time_end = time.time()
    print('Size',m,'x',m,',Method',Method)
    print('Total time:',time_end-time_start)

#20个6x6矩阵
Test(6,20,HouseholderQR.HouQR)
Test(6,20,GivensQR.GivQR)
#20个20x20矩阵
Test(20,20,HouseholderQR.HouQR)
Test(20,20,GivensQR.GivQR)




