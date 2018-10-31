import numpy as np
A=0
for num in range(1,10):
   A=A - 4 * num * np.log(2)
   for i in range(1,num+1):
       A=A+np.log(1+1/(2*i+1)/(2*i-1))
   print(num+1)
   print(np.exp(A))