#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 17 12:25:59 2025

@author: bipin
"""

import xarray as xr
import numpy as np
from config import *
import geopandas as gpd
import rasterio
import matplotlib.pyplot as plt


def get_shapefile_extents(shapefile_path): 
    """ 
    Reads a shapefile and returns its bounds (minx, miny, maxx, maxy).   
    Parameters:
    shapefile_path (str): Path to the shapefile.
    Returns:
    tuple: (minx, miny, maxx, maxy)
    """
    gdf = gpd.read_file(shapefile_path)
    bounds = gdf.total_bounds  # returns (minx, miny, maxx, maxy)    
    return bounds  # Return the bounds directly

def get_data_from_bounds(raster_path, bounds):
    """
    Reads a GeoTIFF or VRT file and extracts data as a matrix from the specified bounds.
    
    Parameters:
    raster_path (str): Path to the GeoTIFF or VRT file.
    bounds (tuple): (minx, miny, maxx, maxy) defining the area of interest.
    
    Returns:
    numpy.ndarray: Data matrix extracted from the specified bounds.
    """
    with rasterio.open(raster_path) as src:
        # Get the window from the bounds
        window = src.window(*bounds)
        data = src.read(1, window=window)  # Read the first band
        
    return data

if __name__ == "__main__":
    print(data_dir_base)
    aoi = get_shapefile_extents(AOI_filename)
    data = get_data_from_bounds(DEM_filename, aoi)
    plt.imshow(data, cmap='terrain')
    plt.colorbar(label='Elevation (m)')
    plt.show()



