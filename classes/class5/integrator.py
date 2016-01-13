import numpy as np

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
