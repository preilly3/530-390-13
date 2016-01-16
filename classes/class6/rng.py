I = 1
a = 65539
c = 0
m = pow(2,31)

def init(m0,a0,c0,I0):
  global I
  global a
  global c
  global m
  I = I0
  a = a0
  c = c0
  m = m0

def lcg():
  global I
  global a
  global c
  global m
  I = (a*I + c) % m
  return float(I / m)
