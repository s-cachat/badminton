import tkinter as tk
import math as math

def calculK():
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


window = tk.Tk()
window.title('Analyse : calcul du coefficient de frottement dynamique')
window.resizable(width=False, height=False)
frm=tk.Frame(master=window)
angleL= tk.Label(master=frm, text="Angle de tir en degrés")
angleL.grid(row=1,column=0)
angleE = tk.Entry(master=frm, width=10)
angleE .grid(row=1,column=1)
v0L= tk.Label(master=frm, text="Vitesse en m/s")
v0L.grid(row=2,column=0)
v0E = tk.Entry(master=frm, width=10)
v0E .grid(row=2,column=1)
xaL= tk.Label(master=frm, text="Distance parcourue en m")
xaL.grid(row=3,column=0)
xaE = tk.Entry(master=frm, width=10)
xaE .grid(row=3,column=1)
y0L= tk.Label(master=frm, text="Hauteur de départ en m")
y0L.grid(row=4,column=0)
y0E = tk.Entry(master=frm, width=10)
y0E .grid(row=4,column=1)
ok = tk.Button(master=frm, text="Calculer",command=calculK)
ok .grid(row=5,column=0)
kL= tk.Label(master=frm, text="Coefficient de frottement fluide k")
kL.grid(row=6,column=0)
kE= tk.Label(master=frm, text="...")
kE.grid(row=6,column=1)

window.mainloop()

