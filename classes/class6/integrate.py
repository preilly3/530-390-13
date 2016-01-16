#!/usr/bin/env python
import integrator as intr
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import rng

#print(intr.trap(intr.cub, 0, 1, 100))

#a = -1
#b = 1
#N = 10000
#h = (b-a) / (N-1)
#x = np.zeros(N)
#for i in range(N):
#  x[i] = a + i*h
#y1 = np.zeros(N)
#y2 = np.zeros(N)
#y1 = intr.legendre(-1,1,x,y1,3)
#y2 = intr.legendre(-1,1,x,y2,5)
#
#print(intr.trap_d(x,intr.multiply(y1,y2)))
#
#plt.plot(x,y1,x,y2)

#[x,w] = intr.gauss_leg(0,1,3)
##print(x,w)
#print(intr.trap(intr.quar,0,1,100))
#print(intr.gauss_quad(intr.quar,x,w))

#rng.init(pow(2,31),65539,0,1)
#N = 10000
#rand1 = np.zeros(N)
#rand2 = np.zeros(N)
#rand3 = np.zeros(N)
#for i in range(N):
#  rand1[i]=rng.lcg()
#  rand2[i]=rng.lcg()
#  rand3[i]=rng.lcg()
#
##plt.scatter(rand1,rand2)
#fig = plt.figure()
#ax = fig.add_subplot(111,projection="3d")
#ax.scatter(rand1,rand2,rand3)
#
#plt.show()

[w,Sw] = intr.monte_carlo_3d(intr.density,[0,-4,-1],[4,4,1],intr.torus,100000)
[x,Sx] = intr.monte_carlo_3d(intr.xmoment,[0,-4,-1],[4,4,1],intr.torus,100000)
[y,Sy] = intr.monte_carlo_3d(intr.ymoment,[0,-4,-1],[4,4,1],intr.torus,100000)
[z,Sz] = intr.monte_carlo_3d(intr.zmoment,[0,-4,-1],[4,4,1],intr.torus,100000)

print(x/w,y/w,z/w)
