# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 22:44:40 2017

@author: Jan Vincent

Note: creating kml file
"""

import simplekml
coordinates_entered=0
kml=simplekml.Kml()
coordinates_requested= int(input("Welcome, Please enter the no of coordinates you want to search:"))
for coordinates_entered in range(0,coordinates_requested):
    requested_longitude=float(input("Enter the longitude"+ str(coordinates_entered)+":"))
    requested_langitude=float(input("Enter the langitude"+str(coordinates_entered)+":"))
    kml.newpoint(name="location"+str(coordinates_entered),coords=[(requested_longitude,requested_langitude)])
kml.save("C:\\Users\\Jan Vincent\\OneDrive\\Python\\Python_For_Beginners\\Generated\Google_location.kml")
