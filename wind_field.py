'''
Create wind component field given inputs for different situations.
'''
import numpy as np

# horizontally homogeneous wind field with linear vertical shear
def horiz_const(usfc, uhgt, zsfc, zhgt, z):
    u = (z-zsfc)/(zhgt-zsfc)*(uhgt-usfc)+usfc
    return u
