# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 21:31:55 2017

@author: Jan Vincent
Note: Print the list using loops
"""

ids=["B3","\nB4","\nB5","\nB6"]


    
with open("C:\\Users\\Jan Vincent\\OneDrive\\Python\\Python_For_Beginners\\text\\test1.txt","w") as file:
    for items in ids:
        print(items)
        file.write(items)