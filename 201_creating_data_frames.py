# -*- coding: utf-8 -*-
"""
Created on Wed Jul  9 15:56:29 2025

@author: subbi
"""
import pandas as pd

#to create an empty daaframe
my_df = pd.DataFrame()

#to create a 1d dataframe
my_df = pd.DataFrame({"Name": ["Tom","Dom","Harry"]})

#to create a mulitple rows and colums dataframe
my_df = pd.DataFrame({"Name": ["Tom","Dom","Harry"],
                      "Id": [201,202,203]})

#to create dataframe from list
my_list = [["Tom","Dom","Om"],
           [201,202,203]]
my_df = pd.DataFrame(my_list, columns=["Name","Id","Id1"])

#to read from csv
my_data=pd.read_excel("grocery_database.xlsx")