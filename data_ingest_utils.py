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
from scipy import ndimage
from skimage import transform


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

def resample_data(data, target_size, method='bilinear'):
    """
    Resamples data to a target size.
    Calculates current resolution from data shape and derives scaling factor.
    
    Parameters:
    data (numpy.ndarray): Input data matrix.
    target_size (tuple): Desired target size as (rows, cols).
    method (str): Interpolation method. Options: 'nearest', 'bilinear', 'bicubic', 'lanczos'.
                  Default is 'bilinear'.
    
    Returns:
    numpy.ndarray: Resampled data matrix.
    """
    # Current size
    current_size = data.shape
    
    # Map method names to scikit-image order parameter
    method_map = {
        'nearest': 0,
        'bilinear': 1,
        'bicubic': 3,
        'lanczos': 4
    }
    
    if method not in method_map:
        raise ValueError(f"Unknown interpolation method: {method}. Choose from {list(method_map.keys())}")    
    # Resample using scikit-image
    resampled_data = transform.resize(data, target_size, order=method_map[method], preserve_range=True)    
    return resampled_data

if __name__ == "__main__":
    print(data_dir_base)
    aoi = get_shapefile_extents(AOI_filename)
    dem_data = get_data_from_bounds(DEM_filename, aoi)
    lulc_data = get_data_from_bounds(LULC_filename, aoi)
    plt.imshow(dem_data, cmap='terrain')
    plt.colorbar(label='Elevation (m)')
    plt.show()



