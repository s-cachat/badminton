import tkinter as tk
import math as math

def calculK():
    alpha = float(alphaE.get())*2*math.pi/360
    v0 = float(v0E.get())
    xa = float(xaE.get())
    y0 = float(y0E.get())
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
        while y>=0 and not math.isinf(y):
            x=x+dt*vx
            y=y+dt*vy
            vx=vx+dt*vx*vx*(-k/m)
            vy=vy+dt*vy*vy*(-k/m)-dt*g
            t=t+dt
            print('x=',x,', t=',t,', y=',y)
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
    kE["text"]=f"{round(k, 8)}"



window = tk.Tk()
window.title('Analyse : calcul du coefficient de frottement fluide')
window.resizable(width=False, height=False)
alphaL= tk.Label(master=window, text="Angle de tir en degrés")
alphaL.grid(row=1,column=0)
alphaE = tk.Entry(master=window, width=10)
alphaE .insert(0,"45")
alphaE .grid(row=1,column=1)
v0L= tk.Label(master=window, text="Vitesse en m/s")
v0L.grid(row=2,column=0)
v0E = tk.Entry(master=window, width=10)
v0E .insert(0,"100")
v0E .grid(row=2,column=1)
xaL= tk.Label(master=window, text="Distance parcourue en m")
xaL.grid(row=3,column=0)
xaE = tk.Entry(master=window, width=10)
xaE .insert(0,"10")
xaE .grid(row=3,column=1)
y0L= tk.Label(master=window, text="Hauteur de départ en m")
y0L.grid(row=4,column=0)
y0E = tk.Entry(master=window, width=10)
y0E .insert(0,"0.3")
y0E .grid(row=4,column=1)
ok = tk.Button(master=window, text="Calculer",command=calculK)
ok .grid(row=5,column=0)
kL= tk.Label(master=window, text="Coefficient de frottement fluide k")
kL.grid(row=6,column=0)
kE= tk.Label(master=window, text="...")
kE.grid(row=6,column=1)

window.mainloop()

