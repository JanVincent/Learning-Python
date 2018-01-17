# -*- coding: utf-8 -*-
"""
Created on Tue Dec 26 11:27:14 2017

@author: Jan Vincent

Note: Generate kml file using data from the csv files
"""

import pandas
import simplekml

df= pandas.read_csv("C:\\Users\\Jan Vincent\\OneDrive\Python\\Python_For_Beginners\\text\\Input_for_kml.csv")
kml=simplekml.Kml()
for longi,lati in zip(df["Longitude"], df["Latitude"]):
    kml.newpoint(coords=[(longi,lati)])
kml.save("C:\\Users\\Jan Vincent\\OneDrive\\Python\\Python_For_Beginners\\Generated\Google_location_from_csv.kml")
