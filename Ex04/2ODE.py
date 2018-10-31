import numpy as np
import matplotlib.pyplot as plt
import RKsolve
#精确解
t=np.linspace(0,1,100)
z=np.exp(2*t)*(np.sin(t)-2*np.cos(t))/5
def eq(t,ini):
    return np.array([1,ini[2],2*ini[2]-2*ini[1]+np.exp(2*t)*np.sin(t)])
r=np.array([0,-0.4,-0.6])
M=RKsolve.RK4(r,0.1,11,eq)
plt.figure()
plt.xlim((-0.1,1.1))
plt.ylim((-0.9,-0.3))
plt.plot(t,z,linewidth=0.5,color="blue")
plt.scatter(M[:,0],M[:,1],s=10,color="red")
label = ["Exact solution","RK4 solution"]
plt.legend(label, loc ='lower center')
plt.grid(True)
plt.show()