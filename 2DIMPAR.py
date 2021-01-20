# Alumno: Torres López Bryan 5U
import matplotlib.pyplot as plt
import numpy as np

plt.axis([0,300,300,0])
plt.axis('on')
plt.grid(True)

# CIRCULO
xc=150
yc=150

r=7*1  # Numero de control 18390021

p1=0*np.pi/180
p2=360*np.pi/180
dp=(p2-p1)/100

xlast=xc+r*np.cos(p1)
ylast=yc+r*np.sin(p1)

for p in np.arange(p1,p2+dp,dp):
    xp=xc+r*np.cos(p)
    yp=yc+r*np.sin(p)
    plt.plot([xlast,xp],[ylast,yp],color=(0,.2,.1),linewidth=2) 
    #Color en base a los 3 ultimos digitos de mi numero de control
    xlast=xp
    ylast=yp

#Primer rectangulo
xc=150 
yc=150

#Esquinas del primer rectangulo
xp=np.array([140,0,0,140])  
yp=np.array([0,0,105,105])

xg1=xc+xp[0] 
yg1=yc+yp[0] 
xg2=xc+xp[1] 
yg2=yc+yp[1] 
xg3=xc+xp[2] 
yg3=yc+yp[2] 
xg4=xc+xp[3] 
yg4=yc+yp[3] 

xg=[xg1,xg2,xg3,xg4,xg1]
yg=[yg1,yg2,yg3,yg4,yg1]
plt.plot(xg,yg,color=(.7,0,.1))


#Segundo rectangulo
xc=220
yc=203

xp=np.array([-150,0,0,-150])  
yp=np.array([0,0,-105,-105])

xg1=xc+xp[0] 
yg1=yc+yp[0] 
xg2=xc+xp[1] 
yg2=yc+yp[1] 
xg3=xc+xp[2] 
yg3=yc+yp[2] 
xg4=xc+xp[3] 
yg4=yc+yp[3] 

xg=[xg1,xg2,xg3,xg4,xg1]
yg=[yg1,yg2,yg3,yg4,yg1]

plt.plot(xg,yg,color=(.1,.7,0))

plt.axes().set_aspect('equal') 
plt.show()