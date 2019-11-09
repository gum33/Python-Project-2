# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 22:58:51 2019

@author: Lenovo
"""

import pandas as pd
import folium

m = folium.Map(
    location=[55.924550, -3.176920],
    zoom_start=15
)
m
cycle_data = pd.read_csv("cyclingtrips_Sep2019.csv")

#print(cycle_data)