#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
import ode
import pde

# ODE
#T = 1
#a = 10
#dt = 0.05
#N = T/dt + 1
#t = np.zeros(N)
#y_euler_exp = np.zeros(N)
#y_euler_imp = np.zeros(N)
#y_ab = np.zeros(N)
#y_rk2 = np.zeros(N)
#Y = np.zeros(N)
#
#t[0] = 0
#y_euler_exp[0] = 1
#y_euler_imp[0] = 1
#y_ab[0] = 1
#y_rk2[0] = 1
#Y[0] = 1
#
#i = 1
#while t[i-1]+dt <= T:
#  t[i] = t[i-1] + dt
#  Y[i] = 1*np.exp(-a*t[i])
#  y_euler_exp[i] = ode.euler_exp(y_euler_exp[i-1],a,dt)
#  y_euler_imp[i] = ode.euler_imp(y_euler_imp[i-1],a,dt)
#  if i < 2:
#    y_ab[i] = ode.euler_exp(y_ab[i-1],a,dt)
#  else:
#    y_ab[i] = ode.ab2(y_ab[i-2],y_ab[i-1],a,dt)
#    y_ab[i] = ode.ab2_corrector(y_ab[i-2],y_ab[i-1],y_ab[i],a,dt)
#  y_rk2[i] = ode.rk2(y_rk2[i-1],a,dt)
#  i = i + 1
#
#plt.plot(t,Y,t,y_euler_exp,t,y_euler_imp,t,y_ab,t,y_rk2)
#plt.show()

# PDE
D = 1
L = 1
T = 1.00
Nx = 100
F = -1
dx = L/(Nx-1)
dt = 0.90*0.5*dx*dx/D
Nt = round(T / dt + 1)

t = np.zeros(Nt)
x = np.zeros(Nx)
u = np.zeros([Nt,Nx])
U = np.zeros(Nx)

for i in range(Nx):
  x[i] = i*dx
  u[0,i] = 0
  U[i] = 0.5*F/D*(x[i]*x[i] - x[i]*L)
  # temperature diffusion initial condition
#  if x[i] >= L/3 and x[i] <= 2*L/3:
#    u[0,i] = 1

i = 1
while t[i-1]+dt <= T:
  t[i] = t[i-1] + dt
  u[i,:] = pde.euler_diffusion(u[i-1,:],D,dt,dx,F)
  # specify boundary condition
  u[i,0] = 0
  u[i,Nx-1] = 0
  i = i + 1

#plt.plot(x,u[0,:],x,u[np.floor(Nt/80),:],x,u[np.floor(5*Nt/40),:],x,u[np.floor(Nt-1),:])
plt.plot(U,x,'o',u[np.floor(Nt/20),:],x,u[np.floor(Nt/10),:],x,u[np.floor(Nt/5),:],x,u[Nt-2,:],x)
plt.show()
