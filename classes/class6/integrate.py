#!/usr/bin/env python
import integrator as intr
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import rng

#Assignment 6 Problem 1
#samples = 100000
#beta = 1
#dist = np.zeros(samples)
#for z in range(samples):
#  dist[z] = intr.exponential(beta)
#
#check = 2
##check is the value whose probability you want to look at
#expected = beta*np.exp(-beta*check)
#print("expected")
#print(expected)
#
##A = np.array([1,1,1,1,1,4,4,4,4,4,4,4,9,9,9])
#A = np.array(dist)
#N = 100
#max_A = np.amax(A)
#min_A = np.amin(A)
#range_of_A = max_A - min_A
#dx = range_of_A / N
#bin_markers = np.zeros(N+1)
#
#for i in range(N+1):
#  bin_markers[i] = min_A + i*dx 
##figures out where the left sides of the bins are in the x domain
#sum_A = 0
#
#bin_counts = np.zeros(N)
#
#for j in range(len(A)):
#  for k in range(N):
#    if A[j] >= bin_markers[k] and A[j] < bin_markers[k+1]:  
#      bin_counts[k]=bin_counts[k] + 1
#      sum_A = sum_A + dx
#      break
#  if A[j] == max_A:
#    bin_counts[N-1]=bin_counts[N-1] + 1
#    sum_A = sum_A + dx
##goes through each value of A and checks if it falls in each of the bins.  If it finds a match, it kicks out of the
##for loop.  If the value is the max(A), it gets added to the counter for the right most bin.
## It also counts up the overall sum of all the bins to do the normalizing below

#sum_div=1/sum_A
#norm_factor = [sum_div]*N
#normalized = intr.multiply(norm_factor,bin_counts)
##normalizes the bin counts so the total sum is 1 for a PDF
##plt.bar(bin_markers[0:len(bin_markers)-1],bin_counts,dx)
#plt.bar(bin_markers[0:len(bin_markers)-1],normalized,dx)

##plt.hist(bin_counts,range/2)
#
#for g in range(N):
#  if check < 0:
#    print("check must be greater than 0")
#  elif check >= bin_markers[g] and check < bin_markers[g+1]:
#    index = g
#    break
#  elif check >= max_A:
#    index = N-1
#sum_check = 0
## finds out which bin the "check" value lies within and spits out the index of that bin location
#for h in range(index+1):
#  sum_check = sum_check+normalized[h]*dx
##sums up the area up until the "check" value
#print("estimated")      
#print(1-sum_check)
#
#plt.show()
#############################

#Assignment 6 Problem 2
[w,Sw] = intr.monte_carlo_3d(intr.density,[-.5,-.5,-1],[1,1,1],intr.sphere,100000)
[x,Sx] = intr.monte_carlo_3d(intr.xmoment,[-.5,-.5,-1],[1,1,1],intr.sphere,100000)
[y,Sy] = intr.monte_carlo_3d(intr.ymoment,[-.5,-.5,-1],[1,1,1],intr.sphere,100000)
[z,Sz] = intr.monte_carlo_3d(intr.zmoment,[-.5,-.5,-1],[1,1,1],intr.sphere,100000)

print("CG of sphere with box (CGx,CGy,CGz)
print(x/w,y/w,z/w)

#print(intr.trap(intr.cub, 0, 1, 100))
##########################

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
#Assignment 6 Problem 2
[w,Sw] = intr.monte_carlo_3d(intr.density,[-.5,-.5,-1],[1,1,1],intr.sphere,100000)
[x,Sx] = intr.monte_carlo_3d(intr.xmoment,[-.5,-.5,-1],[1,1,1],intr.sphere,100000)
[y,Sy] = intr.monte_carlo_3d(intr.ymoment,[-.5,-.5,-1],[1,1,1],intr.sphere,100000)
[z,Sz] = intr.monte_carlo_3d(intr.zmoment,[-.5,-.5,-1],[1,1,1],intr.sphere,100000)

print(x/w,y/w,z/w)
