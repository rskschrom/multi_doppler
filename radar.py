'''
Radar object that has x,y,z position and attributes to simulate velocity field.
'''
import numpy as np

# class for radar object
class Radar:
    def __init__(self, beam_width, xpos, ypos, zpos):
        self.beam_width = beam_width
        self.xpos = xpos
        self.ypos = ypos
        self.zpos = zpos
        self.grid = []

    # generate polar grid for ppi
    def generate_grid_ppi(self, num_range, min_range, max_range,
                          num_azimuth, min_azimuth, max_azimuth, elevation):

        ran1d = np.linspace(min_range, max_range, num_range)
        azi1d = np.linspace(min_azimuth, max_azimuth, num_azimuth)
        ran2d, azi2d = np.meshgrid(ran1d, azi1d, indexing='ij')
        
    # calculate radial velocity field for wind field on radar grid
    def radial_velocity_ppi(self, u_grid, v_grid, w_grid):
