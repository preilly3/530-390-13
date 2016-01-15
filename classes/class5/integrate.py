#!/usr/bin/env python
import integrator as intr
import numpy as np
import matplotlib.pyplot as plt

#print(intr.trap(intr.blah(x,2), 0, 1, 100))
#print(intr.trap(intr.quad, 0, 1, 100))

#a = -1
#b = 1
#N = 10000
#h = (b-a) / (N-1)
#x = np.zeros(N)
#for i in range(N):
#  x[i] = a + i*h
#y1 = np.zeros(N)
#y2 = np.zeros(N)
#y1 = intr.legendre(-1,1,x,y1,5)
#y2 = intr.legendre(-1,1,x,y2,5)
#
#print(intr.trap_d(x,intr.multiply(y1,y2)))
#
#plt.plot(x,y1,x,y2)

#[x,w] = intr.gauss_leg(0,1,2)
#print(intr.trap(intr.quar,0,1,4))
#print(intr.gauss_quad(intr.quar,x,w))

#print(intr.power(2,1))
#plt.show()

###### Problem 1
#my code goes through the various coef terms and calculates the scalar product of the two different sin functions.

#coef = np.array([[1,1],[1,2],[2,8],[8,8]])
#PI = 2.*np.arcsin(1) 
#N=1000
#a = 0
#b = 2*PI
#m = (b-a)/(N-1)
#x = np.zeros(N)
#y1 = np.zeros(N)
#y2 = np.zeros(N)
#size = np.shape(coef)
#for j in range(size[0]):
#  for i in range(N):
#    x[i] = a + m*i
#    y1[i] = np.sin(coef[j,0]*x[i])
#    y2[i] = np.sin(coef[j,1]*x[i])
#  mult=intr.multiply(y1,y2)
#  print(intr.trap_d(x,mult))
#
#####Problem 2
#I wrote a function that calculates the power of x using inputs x and n, for the power. The code goes through for all the x^n terms and then for the exp(x) term.  I needed two slightly different gauss_quad functions to deal with the extra input for my power function.
N = [10, 100, 1000]
n = [1,2,6]
powers = [1,2,11,12]
a = 0
b = 1
for k in range(len(powers)):
  for j in range(len(N)):
    m = (b-a)/(N[j]-1)
    x = np.zeros(N[j])
    y = np.zeros(N[j])
    for i in range(N[j]):
      x[i] = a + m*i
      y[i] = intr.power(x[i],powers[k])
    print(N[j],powers[k])
    print(intr.trap_d(x,y))
  for h in range(len(n)):
    [x2,w] = intr.gauss_leg(a,b,n[h])
    print(N[j], powers[k], n[h])
    print(intr.gauss_quad(intr.power,x2,w,powers[k]))

#exp calculation
for j in range(len(N)):
  m = (b-a)/(N[j]-1)
  x = np.zeros(N[j])
  y = np.zeros(N[j])
  for i in range(N[j]):
    x[i] = a + m*i
    y[i] = np.exp(x[i])
  print(intr.trap_d(x,y))
for h in range(len(n)):
  [x2,w] = intr.gauss_leg(a,b,n[h])
  print(intr.gauss_quad2(np.exp,x2,w))

