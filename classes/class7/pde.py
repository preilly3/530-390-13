import numpy as np

def euler_diffusion(u,D,dt,dx,F):
  Nx = len(u)
  tmp = np.zeros(Nx)
  Ddtdx2 = D*dt/(dx*dx)
  for j in range(1,Nx-1):
    tmp[j] = u[j] + Ddtdx2*(u[j+1]-2*u[j]+u[j-1]) - F*dt
  return tmp
