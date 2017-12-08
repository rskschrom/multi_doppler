import numpy as np
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
from wind_field import horiz_const

# create xyz grid
xmin = -50.
xmax = 50.
ymin = xmin
ymax = xmax
zmin = 0.
zmax = 10.

numx = 50
numy = 50
numz = 10

x1d = np.linspace(xmin, xmax, numx)
y1d = np.linspace(ymin, ymax, numy)
z1d = np.linspace(zmin, zmax, numz)

x3d, y3d, z3d = np.meshgrid(x1d, y1d, z1d, indexing='ij')

# create wind field
u0 = 2.
um = 21.
v0 = 2.
vm = 11.
w0 = 0.
wm = 0.
u = horiz_const(u0, um, zmin, zmax, z3d)
v = horiz_const(v0, vm, zmin, zmax, z3d)
w = horiz_const(w0, wm, zmin, zmax, z3d)

# plot vectors
plt.quiver(x3d[0,:,:], z3d[0,:,:], u[0,:,:], v[0,:,:])
plt.savefig('wind.png')
