'''
Geometry functions for radar code.
'''
import numpy as np

# beam height equation for ppi (every angle in degrees)
def beam_height_ppi(ran, azi, elev, radz):
    erad = np.pi*elev/180.

    ke = 4./3.
    a = 6378137.

    zcor = np.sqrt(ran**2.+(ke*a)**2.+2.*ran*ke*a*np.sin(erad))-ke*a+radz
    scor = ke*a*np.arcsin(ran*np.cos(erad)/(ke*a+zcor))

    xcor = scor*np.cos(np.pi*azi/180.)
    ycor = scor*np.sin(np.pi*azi/180.)
    return xcor, ycor, zcor

