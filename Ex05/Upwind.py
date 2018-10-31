import numpy as np
import math
from matplotlib import pyplot as plt
from matplotlib import animation
#迎风差分格式
def upw(dx,dt,T,a,ini):
    iter=math.ceil(T/dt)
    u=np.zeros((iter,len(ini)))
    u[0]=ini
    for j in range(0,iter-1):
        for k in range(0,len(ini)-1):
            u[j+1,k]=a*dt/dx*u[j,k+1]-(a*dt/dx-1)*u[j,k]
    return u
#选取合适的参数绘制图像
dx=0.05;X=15;n=math.ceil(X/dx)+1;dt=0.04
x=np.linspace(-15,0,n)
#方波初值
v1=np.zeros(n);v2=np.zeros(n)
v1[n-5:n]=np.ones(5)
#高斯波包初值
v2=np.exp(-(x+1)*(x+1)*20)
#绘制图像
M1=upw(dx,dt,12,1,v2)
fig,ax = plt.subplots()
xdata,ydata=[],[]
line1, = ax.plot([], [], lw=2)
tx=ax.text(-14,1.2,'t=%.2f' % 0.,fontsize=14)
def init():
    ax.set_xlim(-15,0)
    ax.set_ylim(-0.5,1.5)
    line1.set_xdata(x)
    ax.set_title('Upwind Method, dx=%.6f,dt=%.6f' % (dx,dt))
    return line1,tx
def animate(i):
    line1.set_ydata(M1[i,])
    tx.set_text('t=%.2f' % (i*dt))
    return line1,tx
anim = animation.FuncAnimation(fig, animate, init_func=init,frames=len(M1),interval=1,blit=True)
plt.grid()
#保存gif
#anim.save('upwind1.gif', writer='imagemagick', fps=30)
plt.show()