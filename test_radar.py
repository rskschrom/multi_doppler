import numpy as np
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.colors as cm
from wind_field import horiz_const
from radar import Radar

# function for creating color map
def createCmap(mapname):
    fil = open(mapname+'.rgb')
    cdata = np.genfromtxt(fil,skip_header=2)
    cdata = cdata/256
    cmap = cm.ListedColormap(cdata, mapname)
    fil.close()
    return cmap

# create radar objects
numran = 51
numazi = 181
minran = 0.
maxran = 50.e3
minazi = 0.
maxazi = 360.
elev = 10.

r1 = Radar(1., 0., 0., 10.)
r1.generate_grid_ppi(numran, minran, maxran, numazi, minazi, maxazi, elev)

r2 = Radar(1., 80.e3, 20.e3, 10.)
r2.generate_grid_ppi(numran, minran, maxran, numazi, minazi, maxazi, elev)

# generate wind field and calculate radial velocity
u0 = 2.
um = 21.
v0 = 2.
vm = 11.
w0 = 0.
wm = 0.
z0 = 0.
zm = 10000.
print np.max(r1.z_grid)

# radar 1
u1 = horiz_const(u0, um, z0, zm, r1.z_grid)
v1 = horiz_const(v0, vm, z0, zm, r1.z_grid)
w1 = horiz_const(w0, wm, z0, zm, r1.z_grid)
vr1 = r1.radial_velocity_ppi(u1, v1, w1)

# radar 2
u2 = horiz_const(u0, um, z0, zm, r2.z_grid)
v2 = horiz_const(v0, vm, z0, zm, r2.z_grid)
w2 = horiz_const(w0, wm, z0, zm, r2.z_grid)
vr2 = r2.radial_velocity_ppi(u2, v2, w2)

# plot radial velocity of each radar
cmap_dir = '/home/meteo/rss5116/research/radar_code/'
vel_map = createCmap(cmap_dir+'vel2_map')
plt.pcolormesh(r1.x_grid, r1.y_grid, vr1, cmap=vel_map, vmin=-50., vmax=50.)
plt.pcolormesh(r2.x_grid, r2.y_grid, vr2, cmap=vel_map, vmin=-50., vmax=50.)

ax = plt.gca()
ax.set_aspect(1.)
plt.colorbar()
plt.savefig('radial_velocity.png')
