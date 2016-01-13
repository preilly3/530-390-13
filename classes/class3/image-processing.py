#!/usr/bin/env python
import improc
import time
import numpy as np
import matplotlib.pyplot as plt
#img = improc.read("gilman-hall.jpg")

# removed red channel
#img_nored = improc.rm_red(img)

# convert to gray
#img_gray_avg = improc.rgb_to_gray_avg(img)
#img_gray_lum = improc.rgb_to_gray_lum(img)

#bigger = improc.scale(img,1.5)
#smaller = improc.scale(bigger,2/3)
#diff = improc.difference(smaller,img)

#improc.show_n([img,smaller,diff])

n = 10000
n_vector=np.arange(0,n+1,1000)
n_vector2=np.array(n_vector)
n_vector2[0]=1
print(n_vector2)
length=len(n_vector2)
time_selectionsort = np.zeros(length)
time_mergesort = np.zeros(length)
for i in range(length):
 A = np.random.rand(n_vector2[i])
 A2 = np.array(A)
 print(i)
 t0 = time.time()
 improc.selectionsort(A,n_vector2[i])
 t1 = time.time()
 improc.mergesort(A2,int(n_vector2[i]))
 t2 = time.time()
 time_selectionsort[i]=t1-t0
 time_mergesort[i]=t2-t1
print(n_vector2)
print(time_selectionsort)
print(time_mergesort)

plt.plot(n_vector2,time_selectionsort,'r',n_vector2,time_mergesort,'b')
plt.xlabel("N")
plt.ylabel("time(s)")
plt.show()

#n=100
#A = np.random.rand(n)
#A2 = np.array(A)
##print(A) 
#t0 = time.time()
#improc.selectionsort(A,n)
#t1 = time.time()
#improc.mergesort(A2,n)
#t2 = time.time()
#print(t1-t0, t2-t1)

#print(improc.factorial(4))

#A = np.array([1,7,1000,5,0,11,8,9,4,2]);
#print(A)
#improc.mergesort(A,10)
#print(A)
#A = np.array([1,7,1000,5,0,11,8,9,4,2]);
#improc.selectionsort(A,10)
#print(A)
#print(improc.binary_search(A,0,8,4))

#kern = [[-1,-1,-1],[-1,8,-1],[-1,-1,-1]]
#kern_G = [[1/16,2/16,1/16],[2/16,4/16,2/16],[1/16,2/16,1/16]]
#gauss = improc.convolution(img,kern_G)
#edges = improc.convolution(gauss,kern)
#improc.show_n([img,edges,gauss])
