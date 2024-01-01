import tkinter as tk
import matplotlib.pyplot as plt
import math as math
def calc():
    alpha = float(alphaE.get())*2*math.pi/360
    k = float(kE.get())
    v0 = float(v0E.get())
    seuil = float(seuilE.get())
    y0 = float(y0E.get())
    m=0.005
    g=9.81
    print("Simulation de vol d'un volant de ",m," kg tiré à ",v0,"m/s avec un angle de ",alpha)
    vx0=v0*math.cos(alpha)
    vy0=v0*math.sin(alpha)
    dt=0.01
    t=0
    x=0
    y=y0
    ymax=0
    xymax=0
    xsmin=0
    xsmax=0
    vx=vx0
    vy=vy0
    plt.clf() 
    while y>=0:
        if ymax<y :
            ymax=y
            xymax=x
        if y>seuil :
            if xsmin==0 :
                xsmin=x
            xsmax=x
        x=x+dt*vx
        y=y+dt*vy
        vx=vx+dt*vx*(-k/m)
        vy=vy+dt*vy*(-k/m)-dt*g
        t=t+dt
        plt.plot(x, y, 'b.:')
    print('Temps de vol (s) : ',t)
    print('Portée du tir (m) : ',x)
    print('Apogee : ',(xymax,ymax))
    print('distances sous le seuil : ',(xsmin,xsmax))
    plt.axis('equal')
    plt.xlim(0,x)
    plt.ylim(0,x)
    plt.show()
    plt.savefig('graph.png')

window = tk.Tk()
window.title('Simulation d''un lancé de volant')
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
kL= tk.Label(master=window, text="Coefficiel de frottement fluide")
kL.grid(row=3,column=0)
kE = tk.Entry(master=window, width=10)
kE .insert(0,"0.03")
kE .grid(row=3,column=1)
y0L= tk.Label(master=window, text="Hauteur de départ en m")
y0L.grid(row=4,column=0)
y0E = tk.Entry(master=window, width=10)
y0E .insert(0,"0.3")
y0E .grid(row=4,column=1)
seuilL= tk.Label(master=window, text="Seuil en m (lob)")
seuilL.grid(row=5,column=0)
seuilE = tk.Entry(master=window, width=10)
seuilE .insert(0,"0.3")
seuilE .grid(row=5,column=1)
ok = tk.Button(master=window, text="Simuler",command=calc)
ok .grid(row=6,column=0)
tvL= tk.Label(master=window, text="Temps de vol (s)")
tvL.grid(row=7,column=0)
tvE= tk.Label(master=window, text="...")
tvE.grid(row=7,column=1)
dpL= tk.Label(master=window, text="Distance parcourue (m)")
dpL.grid(row=8,column=0)
dpE= tk.Label(master=window, text="...")
dpE.grid(row=8,column=1)
apL= tk.Label(master=window, text="Apogée (m)")
apL.grid(row=9,column=0)
apE= tk.Label(master=window, text="...")
apE.grid(row=9,column=1)
dsL= tk.Label(master=window, text="distances au dessus du seuil (m)")
dsL.grid(row=10,column=0)
dsE= tk.Label(master=window, text="...")
dsE.grid(row=10,column=1)

window.mainloop()

