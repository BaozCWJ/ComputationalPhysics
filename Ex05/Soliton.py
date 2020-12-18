import numpy as np
import math
from matplotlib import pyplot as plt
from matplotlib import animation
from numba import jit

#二阶差分
@jit(nopython=True)
def soli(dx,iter,T,delta,ini):
    dt=T/iter;Num=len(ini)
    u=np.zeros((iter,len(ini)))
    u[0]=ini
    for j in range(0,Num):
            u[1,j%Num]=u[0,j%Num]-dt*((u[0,(j+1)%Num]-u[0,(j-1)%Num])/dx/6*(u[0,(j+1)%Num]+u[0,j%Num]+u[0,(j-1)%Num])+delta*delta/dx*(u[0,(j+2)%Num]-2*u[0,(j+1)%Num]+2*u[0,(j-1)%Num]-u[0,(j-2)%Num])/2/dx/dx)
    for i in range(1,iter-1):
        for j in range(0,Num):
            u[i+1,j%Num]=u[(i-1),j%Num]-dt/dx*((u[(i-1),(j+1)%Num]-u[(i-1),(j-1)%Num])/3*(u[(i-1),(j+1)%Num]+u[(i-1),j%Num]+u[(i-1),(j-1)%Num])+delta*delta/dx*(u[(i-1),(j+2)%Num]-2*u[(i-1),(j+1)%Num]+2*u[(i-1),(j-1)%Num]-u[(i-1),(j-2)%Num])/dx)
    return u

#一阶差分
@jit(nopython=True)
def soli1(dx,dt,delta,ini):
    Num=len(ini)
    u=np.zeros(Num)
    for j in range(Num):
        u[j]=ini[j]-dt/dx*((ini[(j+1)%Num]-ini[(j-1)%Num])/6*(ini[(j+1)%Num]+ini[j]+ini[(j-1)%Num])+delta*delta/dx*(ini[(j+2)%Num]-2*ini[(j+1)%Num]+2*ini[(j-1)%Num]-ini[(j-2)%Num])/dx/2)
    return u

#选取合适的参数绘制图形
n=150;X=2;dx=X/n;Num=n+1
L=10000000;T=20;dt=T/L
x=np.linspace(0,2,Num)
v=np.cos(math.pi*x)
K=10000

#绘制图形
fig,ax = plt.subplots()
xdata,ydata=[],[]
line1, = ax.plot([], [], lw=2)
tx=ax.text(1,2.5,'t=%.2f' % 0.,fontsize=10)

#分段测试的迭代函数

def test(Dx,Dt,u,l):
    for j in range(l):
        u = soli1(Dx,Dt,0.022,u)
    return u

def init():
    ax.set_xlim(0,2)
    ax.set_ylim(-3,3)
    line1.set_xdata(x)
    ax.set_title('Soliton, dx=%.7f,dt=%.7f' % (dx,dt))
    return line1,tx

def animate(i):
    global v
    tx.set_text('t=%.2f' % (i*dt))
    line1.set_ydata(v)
    v=test(dx,dt,v,K)
    return line1,tx

anim = animation.FuncAnimation(fig, animate, init_func=init,frames=range(0,L,K),blit=True)
plt.grid()

#保存为gif
anim.save('Soliton5.gif', writer='imagemagick', fps=24)
#plt.show()
