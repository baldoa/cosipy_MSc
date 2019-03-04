import numpy as np
from constants import *
from config import *
import logging

def refreezing(GRID):

    # start module logging
    logger = logging.getLogger(__name__)

    # water refreezed
    water_refreezed = 0.0
    LWCref = 0.0
    
    # Irreducible water when refreezed
    theta_r = 0.0

    total_start = np.sum(GRID.get_liquid_water())

    # Loop over all internal grid points for percolation 
    for idxNode in range(0, GRID.number_nodes-1, 1):
     
        if ((zero_temperature-GRID.get_node_temperature(idxNode)>1e-3) & (GRID.get_node_liquid_water_content(idxNode)>theta_r)):

            # Temperature difference between layer and freezing tempeature
            dT = zero_temperature - GRID.get_node_temperature(idxNode)

            # Compute conversion factor A
            A = (GRID.get_node_specific_heat(idxNode)*GRID.get_node_density(idxNode))/(ice_density*lat_heat_melting)

            # Changes in volumetric contents
            dtheta_i = A * dT
            dtheta_w = -(ice_density/water_density)*dtheta_i
 
            # Check if enough water water to refreeze
            if ((GRID.get_node_liquid_water_content(idxNode)+dtheta_w) < theta_r):
                dtheta_w = -abs(GRID.get_node_liquid_water_content(idxNode) - theta_r)
                dtheta_i = -(water_density/ice_density) * dtheta_w
                dT       = dtheta_i / A
            
            if ((GRID.get_node_ice_fraction(idxNode)+dtheta_i+theta_r) >= 1.0):
                GRID.set_node_liquid_water_content(idxNode, theta_r)
                GRID.set_node_ice_fraction(idxNode, 1.0)
            else:
                GRID.set_node_liquid_water_content(idxNode, GRID.get_node_liquid_water_content(idxNode)+dtheta_w)
                GRID.set_node_ice_fraction(idxNode, GRID.get_node_ice_fraction(idxNode)+dtheta_i)
       
            GRID.set_node_temperature(idxNode, GRID.get_node_temperature(idxNode)+dT)
        
        else:
            
            dtheta_i = 0
            dtheta_w = 0
    
        GRID.set_node_refreeze(idxNode, dtheta_i*GRID.get_node_height(idxNode)) 
        water_refreezed =  water_refreezed - dtheta_w*GRID.get_node_height(idxNode)        
    
    total_end = np.sum(GRID.get_liquid_water())
    
    if (total_start-total_end-water_refreezed) > 1e-8:
        logger.error('Refreezing module is not mass consistent')
        logger.error('Water in the begin/end/refreezed: %2.7f /  %2.7f / %2.7f' % (total_start,total_end,water_refreezed))
    
    return water_refreezed


