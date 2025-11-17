#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 17 12:27:26 2025

@author: bipin
"""

import os

data_dir_base   = os.path.join(os.path.dirname(__file__), 'data')
AOI_filename  = os.path.join(data_dir_base, 'AOI_1.shp')
DEM_filename = os.path.join(data_dir_base, 'DEM/combined.vrt')


if not os.path.exists(data_dir_base):
    os.makedirs(data_dir_base)
