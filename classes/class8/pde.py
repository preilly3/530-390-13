import numpy as np

def euler_diffusion(u,D,dt,dx,F):
  Nx = len(u)
  tmp = np.zeros(Nx)
  Ddtdx2 = D*dt/(dx*dx)
  for j in range(1,Nx-1):
    tmp[j] = u[j] + Ddtdx2*(u[j+1]-2*u[j]+u[j-1]) - F*dt
  return tmp

def jacobi(u,f,dx,Nx,Ny,itmax):
  x = np.zeros(Nx*Ny)
  for j in range(Ny):
    for i in range(Nx):
      x[i+j*Nx] = u[i+j*Nx]
  for it in range(itmax):
    for j in range(1,Ny-1):
      for i in range(1,Nx-1):
        x[i+j*Nx] = 0.25 * (x[(i-1) + j*Nx] \
                          + x[(i+1) + j*Nx] \
                          + x[i + (j-1)*Nx] \
                          + x[i + (j+1)*Nx] \
                          - dx*dx*f[i + j*Nx])
  return x

def Au(A,u):
  n = len(u)
  tmp = np.zeros(n)
  for q in range(n):
    for p in range(n):
      tmp[q] = tmp[q] + A[p,q]*u[p]
  return tmp

def bsc(b,c):
  n = len(b)
  sub = np.zeros(n)
  for p in range(n):
    sub[p] = b[p] - c[p]
  return sub

def norm2(u):
  n = len(u)
  norm = 0
  for p in range(n):
    norm = norm + u[p]*u[p]
  return np.sqrt(norm)
