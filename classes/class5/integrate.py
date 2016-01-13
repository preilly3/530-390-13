#!/usr/bin/env python
import integrator as intr
import numpy as np
import matplotlib.pyplot as plt

#print(intr.trap(intr.lin, 0, 1, 100))

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

[x,w] = intr.gauss_leg(0,1,2)
print(intr.trap(intr.quar,0,1,4))
print(intr.gauss_quad(intr.quar,x,w))

#plt.show()
