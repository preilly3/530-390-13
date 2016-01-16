import numpy as np
import random

PI = 2.*np.arcsin(1)

def trap(func, a, b, N):
  h = (b-a) / (N-1)
  S = 0.5*(func(a) + func(b))
  x = a + h
  for j in range(1,N-1):
    S = S + func(x)
    x = x + h
  S = S*h
  return S

def trap_d(x, y):
  N = len(x)
  h = (x[N-1]-x[0]) / (N-1)
  S = 0.5*(y[0] + y[N-1])
  for j in range(1,N-1):
    S = S + y[j]
  S = S*h
  return S

def lin(x):
  return x

def quad(x):
  return x*x

def cub(x):
  return x*x*x

def quar(x):
  return x*x*x*x

def legendre(a,b,x,y,n):
  if n == 0:
    return np.ones(len(x))
  if n == 1:
    return x
  N = len(x)
  tmp = np.zeros(N)
  P_1 = legendre(a,b,x,y,n-1)
  P_2 = legendre(a,b,x,y,n-2)
  for i in range(N):
    tmp[i] = (2.*n-1)*x[i]*P_1[i] - (n-1)*P_2[i]
    tmp[i] = tmp[i] / n
  return tmp

def multiply(A,B):
  N = len(A)
  tmp = np.zeros(N)
  for i in range(N):
    tmp[i] = A[i]*B[i]
  return tmp

def gauss_leg(a, b, N):
  x = np.zeros(N)
  w = np.zeros(N)
  eps = 1.e-14
  m = (N+1) >> 1
  xm = 0.5*(b+a)
  xl = 0.5*(b-a)
  for i in range(m):
    z = np.cos(PI*(i+0.75)/(N+0.5))
    z1 = z + 1.
    while (abs(z-z1) > eps):
      p1 = 1.
      p2 = 0.
      for j in range(N):
        p3 = p2
        p2 = p1
        p1 = ((2.*j+1) * z * p2 - j * p3) / (j+1)
      pp = N * (z * p1 - p2) / (z * z - 1.)
      z1 = z
      z = z1 - p1 / pp
    x[i] = xm - xl*z
    x[N-1-i] = xm + xl*z
    w[i] = 2.*xl / ((1.-z*z) * pp*pp)
    w[N-1-i] = w[i]
  return [x,w]

def gauss_quad(func,x,w):
  N = len(x)
  I = 0
  for i in range(N):
    I = I + w[i]*func(x[i])
  return I

def monte_carlo_1d(func,a,b,N):
  f = 0
  f2 = 0
  L = b-a
  for i in range(N):
    x = a + random.random()*L
    f = f + func(x)
    f2 = f2 + func(x)*func(x)
  f = f / N
  f2 = f2 / N
  I = f / L
  S = np.sqrt((f2 - f*f) / N) * L
  return [I,S]

def monte_carlo_3d(func,a,b,inregion,N):
  f = 0
  f2 = 0
  Lx = b[0]-a[0]
  Ly = b[1]-a[1]
  Lz = b[2]-a[2]
  for i in range(N):
    x = a[0] + random.random()*Lx
    y = a[1] + random.random()*Ly
    z = a[2] + random.random()*Lz
    if inregion(x,y,z):
      f = f + func(x,y,z)
      f2 = f2 + func(x,y,z)*func(x,y,z)
  f = f / N
  f2 = f2 / N
  I = f * Lx*Ly*Lz
  S = np.sqrt((f2-f*f) / N) * Lx*Ly*Lz
  return [I,S]
  
def sphere(x,y,z):
  if x*x + y*y + z*z <= 1:
    return True
  else:
    return False

def torus(x,y,z):
  if z*z + pow((np.sqrt(x*x+y*y)-3),2) <= 1:
    return True
  else:
    return False

def density(x,y,z):
  return 1.

def xmoment(x,y,z):
  return x

def ymoment(x,y,z):
  return y

def zmoment(x,y,z):
  return z

def exponential(beta):
  tmp = random.random()
  if tmp == 0:
    tmp = random.random()
  else:
    return -np.log(tmp)/beta
