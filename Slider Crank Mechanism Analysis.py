import numpy as np
from numpy import sin, cos, pi, sqrt
import matplotlib.pyplot as plt
from scipy.misc import  derivative

a2=75 #crank lenght
a3=300  #connecting rod lenght

n= 500  # rpm
w= (2*pi*n)/60 #radian per second
#s14: slider displacement
def displacement(t):
    d1=a2*cos(w*t)
    d2=sqrt((a3**2-(a2**2*sin(w*t)*sin(w*t))))
    return d1+d2
time=np.linspace(0,0.5,300)
theta12=w*time*180/pi

x=displacement(time)

def velocity(t):
    return  derivative(displacement,t)
v=velocity(time)

def acceleration(t):
    return derivative(velocity, t)
a=acceleration(time)

fig=plt.figure()
ax1=fig.add_subplot(3,1,1)
ax1.plot(theta12,x, color="blue")
ax1.set(xlim=(0,720))
ax1.set_ylabel("Displacement")
ax1.set_xlabel("Theta12")

ax2=fig.add_subplot(3,1,2)
ax2.plot(theta12,v, color="red")
ax2.set(xlim=(0,720))
ax2.set_ylabel("Velocity")
ax2.set_xlabel("Theta12")

ax3=fig.add_subplot(3,1,3)
ax3.plot(theta12,a, color="green")
ax3.set(xlim=(0,720))
ax3.set_ylabel("Acceleration")
ax3.set_xlabel("Theta12")


plt.show()