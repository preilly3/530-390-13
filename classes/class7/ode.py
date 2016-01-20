def euler_exp(y,a,dt):
  return (1-a*dt)*y

def euler_imp(y,a,dt):
  return y/(1+a*dt)

def ab2(y0,y,a,dt):
  return y - 0.5*dt*(3*a*y - a*y0)

def ab2_corrector(y0,y,y1,a,dt):
  return y - dt/12 * (5*a*y1 + 8*a*y - a*y0)

def rk2(y,a,dt):
  ymid = y - 0.5*dt*a*y
  return y - dt*a*ymid
