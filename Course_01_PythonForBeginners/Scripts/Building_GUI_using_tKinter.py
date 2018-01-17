# -*- coding: utf-8 -*-
"""
Created on Tue Dec 26 11:53:46 2017

@author: Jan Vincent

Note: Building GUI with tKinter lib
"""

import tkinter
import pandas
import simplekml
from tkinter.filedialog import askopenfilename

def browse():
    global input_file
    input_file=askopenfilename()
def KMLGeneration(output_file="C:\\Users\\Jan Vincent\\OneDrive\\Python\\Python_For_Beginners\\Generated\Google_location_from_GUI.kml"):   
    df= pandas.read_csv(input_file)
    kml = simplekml.Kml()
    for long,lat in zip(df["Longitude"],df["Latitude"]):
        kml.newpoint(coords=[(long,lat)])
    kml.save(output_file)    
roof = tkinter.Tk()
roof.title("KML generator")
label=tkinter.Label(roof, text="Generate the KML files")
label.pack()
browseButton=tkinter.Button(roof,text="Browse",command=browse)
browseButton.pack()
KMLButton=tkinter.Button(roof,text="Generate KML file",command=KMLGeneration)
KMLButton.pack()
roof.mainloop()
