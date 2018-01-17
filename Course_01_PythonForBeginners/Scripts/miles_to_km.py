# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 17:46:29 2017

@author: Jan Vincent

Note: Miles to Kilometer conversion
"""
def miletokm_conversion(miles):
    km=miles*1.60934
    return km

print("Miles to Kilometer Convertor")
User_input_miles=float(input("Please enter the no of miles:"))
print(miletokm_conversion(User_input_miles),"km")
