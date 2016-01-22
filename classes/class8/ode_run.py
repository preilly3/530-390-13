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
#D = 1
#L = 1
#T = 1.00
#Nx = 100
#F = -1
#dx = L/(Nx-1)
#dt = 0.90*0.5*dx*dx/D
#Nt = round(T / dt + 1)
#
#t = np.zeros(Nt)
#x = np.zeros(Nx)
#u = np.zeros([Nt,Nx])
#U = np.zeros(Nx)
#
#for i in range(Nx):
#  x[i] = i*dx
#  u[0,i] = 0
#  U[i] = 0.5*F/D*(x[i]*x[i] - x[i]*L)
#  # temperature diffusion initial condition
##  if x[i] >= L/3 and x[i] <= 2*L/3:
##    u[0,i] = 1
#
#i = 1
#while t[i-1]+dt <= T:
#  t[i] = t[i-1] + dt
#  u[i,:] = pde.euler_diffusion(u[i-1,:],D,dt,dx,F)
#  # specify boundary condition
#  u[i,0] = 0
#  u[i,Nx-1] = 0
#  i = i + 1
#
##plt.plot(x,u[0,:],x,u[np.floor(Nt/80),:],x,u[np.floor(5*Nt/40),:],x,u[np.floor(Nt-1),:])
#plt.plot(U,x,'o',u[np.floor(Nt/20),:],x,u[np.floor(Nt/10),:],x,u[np.floor(Nt/5),:],x,u[Nt-2,:],x)
#plt.show()

# Poisson problem
Lx = 10
Ly = 4

Nx =101
Ny = 41
#back calculated Nx and Ny to get dx and dy = 0.1
dx = Lx/(Nx-1)
dy = Ly/(Ny-1)

d2dx2 = 1/(dx*dx)

u = np.zeros(Nx*Ny)
f = np.zeros(Nx*Ny)

# set forcing
i = np.floor(0.5*Nx)
j = np.floor(0.5*Ny)
f[i + j*Nx] = 10

# boundary conditions
for j in range(Ny):
  i = 0
  u[i+j*Nx] = 1
  i = Nx-1
  u[i+j*Nx] = 0
for i in range(Nx):
  j = 0
  u[i+j*Nx] = 0
  j = Ny-1
  u[i+j*Nx] = 0

# Jacobi iteration
u = pde.jacobi(u,f,dx,Nx,Ny,1000)

# check error
# (build matrix)
nx = Nx - 2
ny = Ny - 2
A = np.zeros([nx*ny,nx*ny])
for q in range(nx*ny):
  for p in range(nx*ny):
    if p == q:
      A[p,q] = -4*d2dx2
    elif p == q-1:
      A[p,q] = 1*d2dx2
    elif p == q+1:
      A[p,q] = 1*d2dx2
    elif p == q-nx:
      A[p,q] = 1*d2dx2
    elif p == q+nx:
      A[p,q] = 1*d2dx2

# boundary conditions
for q in range(nx*ny):
  for p in range(nx*ny):
    if p % nx == nx-1 and q % ny == 0:
      A[p,q] = 0
    if p % nx == 0 and q % ny == ny-1:
      A[p,q] = 0

#plt.imshow(A,interpolation="none")
#plt.show()

# pull out the interior
u_int = np.zeros(nx*ny)
f_int = np.zeros(nx*ny)
for j in range(ny):
  for i in range(nx):
    u_int[i+j*nx] = u[(i+1) + (j+1)*Nx]
    f_int[i+j*nx] = f[(i+1) + (j+1)*Nx]

# (calculate error) ** DOES NOT WORK FOR NONZERO BOUNDARY CONDITIONS **
b_tilde = pde.Au(A,u_int)
norm = pde.norm2(pde.bsc(f_int,b_tilde))
print(norm)

# plot
u_plot = np.zeros([Nx,Ny])
f_plot = np.zeros([Nx,Ny])
for j in range(Ny):
  for i in range(Nx):
    u_plot[i,j] = u[i+j*Nx]
    f_plot[i,j] = f[i+j*Nx]

x = np.zeros([Nx+1,Ny+1])
y = np.zeros([Nx+1,Ny+1])
for j in range(Ny+1):
  for i in range(Nx+1):
    x[i,j] = -0.5*dx + i*dx
    y[i,j] = -0.5*dy + j*dy

plt.pcolormesh(x,y,u_plot,edgecolors="black")
plt.colorbar()
plt.show()
