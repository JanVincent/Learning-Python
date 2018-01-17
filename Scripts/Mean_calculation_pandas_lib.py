# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 21:59:52 2017

@author: Jan Vincent

Note: Mean calculation using pandas library
"""
import pandas
import glob2


def mean_calculation(file_path):
    data_frame=pandas.read_csv(file_path)
    mean_file=data_frame.mean()
    print(float(mean_file))

file_path=glob2.glob("C:\\Users\\Jan Vincent\\OneDrive\\Python\\Python_For_Beginners\\text\*.txt")

for every_file in file_path:
    mean_calculation(every_file)
