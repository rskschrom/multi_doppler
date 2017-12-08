'''
Radar object that has x,y,z position and attributes to simulate velocity field.
'''
import numpy as np
from geometry import beam_height_ppi

# class for radar object
class Radar:
    def __init__(self, beam_width, xpos, ypos, zpos):
        self.beam_width = beam_width
        self.xpos = xpos
        self.ypos = ypos
        self.zpos = zpos
        self.ran_grid = []
        self.azi_grid = []
        self.elev_grid = []
        self.x_grid = []
        self.y_grid = []
        self.z_grid = []

    # generate polar grid for ppi
    def generate_grid_ppi(self, num_range, min_range, max_range,
                          num_azimuth, min_azimuth, max_azimuth, elevation):

        ran1d = np.linspace(min_range, max_range, num_range)
        azi1d = np.linspace(min_azimuth, max_azimuth, num_azimuth)
        ran_grid, azi_grid = np.meshgrid(ran1d, azi1d, indexing='ij')
        x_grid, y_grid, z_grid = beam_height_ppi(ran_grid, azi_grid, elevation, self.zpos)

        self.ran_grid = ran_grid      
        self.azi_grid = azi_grid
        self.elev_grid = elevation     
        self.x_grid = x_grid        
        self.y_grid = y_grid        
        self.z_grid = z_grid   
        return       

    # calculate radial velocity field for wind field on radar grid
    def radial_velocity_ppi(self, u_grid, v_grid, w_grid):
        azi_rad = np.pi*self.azi_grid/180.
        elev_rad = np.pi*self.elev_grid/180.
        vr = u_grid*np.cos(azi_rad)*np.cos(elev_rad)+\
             v_grid*np.sin(azi_rad)*np.cos(elev_rad)+w_grid*np.sin(elev_rad)
        return vr


