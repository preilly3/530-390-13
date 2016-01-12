#!/usr/bin/env python
import improc
import numpy as np
import time
import matplotlib.pyplot as plt

N = [100,1000,10000]
t_selection = np.zeros(len(N))
t_merge = np.zeros(len(N))

n = 10000
x = np.zeros(n)
N_squared = np.zeros(n)
N_log_N = np.zeros(n)

print("Ratios (selection/merge):")
for i in range(len(N)):
  A = np.random.rand(N[i])
  A2 = np.array(A)
  t0 = time.time()
  improc.selectionsort(A,N[i])
  t1 = time.time()
  improc.mergesort(A2,N[i])
  t2 = time.time()
  t_selection[i] = t1 - t0
  t_merge[i] = t2 - t1
  print(t_selection[i]/t_merge[i])
for i in range(1,n):
  x[i] = i
  N_squared[i] = 1.55e-7*x[i]*x[i]
  N_log_N[i] = 1.5e-6*x[i]*np.log2(x[i])

plt.plot(N,t_selection,'ro',N,t_merge,'bo',x,N_squared,'r',x,N_log_N,'b')
plt.xlabel("N")
plt.ylabel("runtime (seconds)")
plt.legend(["selection sort", "merge sort", r"$N^2$", r"$N\log_2 N$"],
loc="upper left")
plt.show()
