import matplotlib.pyplot as plt
import math as math
print("Simulation de vol d'un volant de 5g : calcul de k")
alpha = float(input("Angle de tir en degrés : "))*2*math.pi/360
v0 = float(input("Vitesse en m/s : "))
xa = float(input("Distance parcourue en m: "))
y0 = float(input("hauteur du point de départ en m: "))
k=0.001
dk=0.1
first=0
m=0.005
g=9.81
vx0=v0*math.cos(alpha)
vy0=v0*math.sin(alpha)
dt=0.01
while dk>0.000001:
    t=0
    x=0
    y=y0
    vx=vx0
    vy=vy0
    while y>=0:
        x=x+dt*vx
        y=y+dt*vy
        vx=vx+dt*vx*(-k/m)
        vy=vy+dt*vy*(-k/m)-dt*g
        t=t+dt
    if first==1:
        dk=dk*0.5
    if x<xa:
        first=1
        print('- k=',k,', x=',x,', t=',t,', xa=',xa)
        k=k-dk
    else:
        print('+ k=',k,', x=',x,', t=',t,', xa=',xa)
        k=k+dk
print('Le coefficient de frottement fluide est k=',k)
