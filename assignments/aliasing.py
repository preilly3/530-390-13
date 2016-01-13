#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
import fft

PI = 2.*np.arcsin(1)

N = 64
L = 2.*PI
dx = L / (N-1)
x = np.zeros(N)
f = np.zeros(N)
f_04 = np.zeros(2*N)
f_13 = np.zeros(2*N)
f_28 = np.zeros(2*N)
f_39 = np.zeros(2*N)
f_50 = np.zeros(2*N)

for i in range(N):
  x[i] = i*dx
  f[i] = i
for i in range(N):
  f_04[2*i] = np.sin(x[i]) + np.sin(4.*x[i])
  f_13[2*i] = np.sin(x[i]) + np.sin(13.*x[i])
  f_28[2*i] = np.sin(x[i]) + np.sin(28.*x[i])
  f_39[2*i] = np.sin(x[i]) + np.sin(39.*x[i])
  f_50[2*i] = np.sin(x[i]) + np.sin(50.*x[i])

fft.fft(f_04,1.)
fft.fft(f_13,1.)
fft.fft(f_28,1.)
fft.fft(f_39,1.)
fft.fft(f_50,1.)

fft.plot_i_n([f[:0.5*N],f[:0.5*N],f[:0.5*N],f[:0.5*N],f[:0.5*N]],
[f_04[:N],f_13[:N],f_28[:N],f_39[:N],f_50[:N]],["4","13","28","39","50"])

plt.show()
