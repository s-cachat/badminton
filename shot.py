import matplotlib.pyplot as plt
import math as math
k=float(input("Coefficient de frottements en kg/s : "))
alpha = 45
m=0.005
g=9.81
v0=100
print("Simulation de vol d'un boulet de ",m," kg tiré à ",v0,"m/s avec un angle de ",alpha)
vx0=v0*math.cos(alpha)
vy0=v0*math.sin(alpha)
dt=0.01
t=0
x=0
y=0
ymax=0
xymax=0
vx=vx0
vy=vy0
plt.clf() 
while y>=0:
    if ymax<y :
        ymax=y
        xymax=x
    x=x+dt*vx
    y=y+dt*vy
    vx=vx+dt*vx*(-k/m)
    vy=vy+dt*vy*(-k/m)-dt*g
    t=t+dt
    plt.plot(x, y, 'b.:')
print('Temps de vol (s) : ',t)
print('Portée du tir (m) : ',x)
print('Apogee : ',(xymax,ymax))
plt.axis('equal')
plt.xlim(0,x)
plt.ylim(0,x)
plt.show()
plt.savefig('graph.png')
