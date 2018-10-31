import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import RKsolve
#精确解
r=np.array([0,0,0,0,2,0.1])
t=np.linspace(0,80,8000)
x=np.zeros(len(t));y=np.zeros(len(t))
for k in range(len(t)):
    x[k]=-2*np.cos(t[k])+2;y[k]=2*np.sin(t[k])
z=0.1*t
def g(t,ini):
    w=1
    return np.array([ini[3],ini[4],ini[5],w*ini[4],-w*ini[3],0])
#二阶欧拉插值
def Euler2(ini,step,iter):
    x=np.zeros(iter);y=np.zeros(iter);z=np.zeros(iter)
    vx=np.zeros(iter);vy=np.zeros(iter)
    x[0]=ini[0];y[0]=ini[1];z[0]=ini[2]
    vx[0]=ini[3];vy[0]=ini[4];vz=ini[5]
    for k in range(iter-1):
        x[k+1]=x[k]+step*vx[k]+step*step*vy[k]/2
        y[k+1]=y[k]+step*vy[k]-step*step*vx[k]/2
        vx[k+1]=vx[k]+step*vy[k]-step*step*vx[k]/2
        vy[k+1]=vy[k]-step*vx[k]-step*step*vy[k]/2
        z[k+1]=z[k]+step*vz
    return x,y,z
#绘图展示
fig=plt.figure()
ax = Axes3D(fig)
x1,y1,z1=Euler2(r,0.01,8000)
M=RKsolve.RK4(r,0.01,8000,g)
ax.set_xlim((-0.5,4.5))
ax.set_ylim((-2.5,2.5))
ax.set_zlim((-0.5,8.5))
ax.plot(x1,y1,z1,linewidth=0.5,color="blue")
ax.plot(M[:,0],M[:,1],M[:,2],linewidth=0.5,color="red")
ax.plot(x,y,z,linewidth=0.5,color="green")
label = ["Euler solution","RK4 solution","Exact solution"]
plt.legend(label, loc ='lower center')
plt.grid(True)
plt.show()