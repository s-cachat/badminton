import tkinter as tk
import matplotlib.pyplot as plt
import math as math
import numpy as np

from matplotlib.backend_bases import key_press_handler
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
                                               NavigationToolbar2Tk)
from matplotlib.figure import Figure

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
    datax=np.array([0])
    datay=np.array([y0])
    ax.clear()
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
        print((x,y))
        vx=vx+dt*vx*vx*(-k/m)
        vy=vy+dt*vy*vy*(-k/m)-dt*g
        t=t+dt
        datax=np.append(datax,[x])
        datay=np.append(datay,[y])
    tvE["text"]=f"{round(t, 2)}"
    dpE["text"]=f"{round(x, 2)}"
    apE["text"]=f"x={round(x, 2)} y={round(y, 2)}"
    dsE["text"]=f"{round(xsmin, 2)}  -> {round(xsmax, 2)}"

    ax.plot(datax,datay)
    ax.plot([xsmin,xsmin,xsmax,xsmax],[0,seuil,seuil,0])
    ax.set_xlim(0,x)
    ax.set_ylim(0,ymax)
    canvas.draw()


window = tk.Tk()
window.title('Simulation d''un lancé de volant')
window.resizable(width=False, height=False)
frm=tk.Frame(master=window)
frm .grid(row=0,column=0)
alphaL= tk.Label(master=frm, text="Angle de tir en degrés")
alphaL.grid(row=1,column=0)
alphaE = tk.Entry(master=frm, width=10)
alphaE .insert(0,"45")
alphaE .grid(row=1,column=1)
v0L= tk.Label(master=frm, text="Vitesse en m/s")
v0L.grid(row=2,column=0)
v0E = tk.Entry(master=frm, width=10)
v0E .insert(0,"100")
v0E .grid(row=2,column=1)
kL= tk.Label(master=frm, text="Coefficiel de frottement fluide")
kL.grid(row=3,column=0)
kE = tk.Entry(master=frm, width=10)
kE .insert(0,"0.03")
kE .grid(row=3,column=1)
y0L= tk.Label(master=frm, text="Hauteur de départ en m")
y0L.grid(row=4,column=0)
y0E = tk.Entry(master=frm, width=10)
y0E .insert(0,"0.3")
y0E .grid(row=4,column=1)
seuilL= tk.Label(master=frm, text="Seuil en m (lob)")
seuilL.grid(row=5,column=0)
seuilE = tk.Entry(master=frm, width=10)
seuilE .insert(0,"3")
seuilE .grid(row=5,column=1)
ok = tk.Button(master=frm, text="Simuler",command=calc)
ok .grid(row=6,column=0)
tvL= tk.Label(master=frm, text="Temps de vol (s)")
tvL.grid(row=7,column=0)
tvE= tk.Label(master=frm, text="...")
tvE.grid(row=7,column=1)
dpL= tk.Label(master=frm, text="Distance parcourue (m)")
dpL.grid(row=8,column=0)
dpE= tk.Label(master=frm, text="...")
dpE.grid(row=8,column=1)
apL= tk.Label(master=frm, text="Apogée (m)")
apL.grid(row=9,column=0)
apE= tk.Label(master=frm, text="...")
apE.grid(row=9,column=1)
dsL= tk.Label(master=frm, text="distances au dessus du seuil (m)")
dsL.grid(row=10,column=0)
dsE= tk.Label(master=frm, text="...")
dsE.grid(row=10,column=1)

fig = Figure(figsize=(5, 4), dpi=100)
ax = fig.add_subplot()
canvas = FigureCanvasTkAgg(fig, master=window)
canvas.draw()
canvas.get_tk_widget().grid(row=1,column=0)



window.mainloop()

