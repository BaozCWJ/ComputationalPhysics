import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import RKsolve
r1=np.array([12,4,0,10,28,5/3])
r2=np.array([12,4,0,10.1,28,5/3])
r3=np.array([12,4,0,10,28.1,5/3])
r4=np.array([12,4,0,10,28.1,5/3+0.1])
def L(t,ini):
    return np.array([-ini[5]*ini[0]+ini[2]*ini[1],-ini[3]*ini[1]+ini[3]*ini[2],-ini[1]*ini[0]+ini[4]*ini[1]-ini[2],0,0,0])
plt.figure()
N1=RKsolve.RK4(r1,0.001,10000,L)
N2=RKsolve.RK4(r2,0.001,10000,L)
N3=RKsolve.RK4(r3,0.001,10000,L)
N4=RKsolve.RK4(r4,0.001,10000,L)
plt.subplot(221,projection='3d')
plt.plot(N1[:,0],N1[:,1],N1[:,2],linewidth=0.5,color="red")
plt.subplot(222,projection='3d')
plt.plot(N2[:,0],N2[:,1],N2[:,2],linewidth=0.5,color="blue")
plt.subplot(223,projection='3d')
plt.plot(N3[:,0],N3[:,1],N3[:,2],linewidth=0.5,color="green")
plt.subplot(224,projection='3d')
plt.plot(N4[:,0],N4[:,1],N4[:,2],linewidth=0.5,color="black")
plt.grid(True)
plt.show()