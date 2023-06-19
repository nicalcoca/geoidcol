#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 20:45:18 2023

@author: nicalcoca
"""

from .models import Project

import pandas as pd
import geopandas as gpd
import os

## Lector de archivos de gravimetría y altimetría
def reader(wd, file, tipo, aggregator=None):

    file_name, file_ext = os.path.splitext(file)
    
    os.chdir(wd)
    
    ## Archivos .csv
    if file_ext == '.csv':
        
        df = pd.read_csv(file, delimiter=',')
    
    ## Archivos .shp
    elif file_ext == '.shp' or file_ext == '.gpkg':
        
        gdf = gpd.read_file(file)
        df = pd.DataFrame(gdf)
        
    ## El resto de archivos
    else:
        
        return 'Formato no soportado'
    
    ## Crea objeto de clase Proyecto
    return Project(file, df, tipo)