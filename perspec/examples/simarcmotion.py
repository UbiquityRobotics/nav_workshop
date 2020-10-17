import numpy as np
import matplotlib.pyplot as pl

pl.style.use('dark_background')

L = 10
N = 100
F = 5

ran = np.random.random
rann = np.random.normal

x = -L + 2*L*ran(N)
y =  F - 2*L*ran(N)
z =  2*F + 2*L*ran(N)

R = -4*L
ds = 1

cs = np.cos(ds/R)
sn = np.sin(ds/R)

xp =  cs*(x+R) + sn*z - R
yp = y
zp = -sn*(x+R) + cs*z 

X = x/z
Y = y/z

dX = xp/zp - x/z
dY = yp/zp - y/z

dXa = (X/z + (1+X*X)/R) * ds
dYa = (Y/z + X*Y/R) * ds

pl.plot(X,-Y,'.',color='cyan')
pl.plot(X+dX,-(Y+dY),'.',color='magenta')
pl.plot(X+dXa,-(Y+dYa),'.',color='yellow')

errlev = 0.1
dX *= 1 + errlev*rann(size=N)
dY *= 1 + errlev*rann(size=N)
z1 = X / (dX/ds - (1+X*X)/R)
z2 = Y / (dY/ds - X*Y/R)

pl.gca().set_aspect('equal')
pl.show()

za = (z1+z2)/2
ze = np.abs(z1-z2)

pl.plot(z,za,'.',color='gray')
small = ze/z < errlev
za = za[small]
z = z[small]
pl.plot(z,za,'.',color='white')

pl.xlim(0,2*(F+L))
pl.ylim(0,2*(F+L))
pl.gca().set_aspect('equal')
pl.show()
