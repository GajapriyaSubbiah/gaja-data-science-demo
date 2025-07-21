# -*- coding: utf-8 -*-
"""
Created on Thu Jul 17 14:38:47 2025

@author: subbi
"""

import pandas as pd

df_a = pd.DataFrame({"userId": [1,2,3,5,7],
         "Age": [40,51,15,25,41]})
df_b = pd.DataFrame({"userId": [1,2,3,4,5],
         "Gender": ["m","f","f","m","m"],
         "Age": [40,51,16,20,41]})
transactions = pd.read_excel("grocery_database.xlsx", sheet_name="transactions")
product_areas = pd.read_excel("grocery_database.xlsx", sheet_name="product_areas")
#joining

# append and concat are the same but concat is most commonly used

df_c = pd.concat([df_a,df_b], axis=1)
df_d = pd.concat([df_a,df_b], axis=0)

#merging
#like sql, inner, left, outer we have
#inner ----> both values should be in both tables
pd.merge(df_a,df_b, how="inner", on="userId")

#left ---->
pd.merge(df_a,df_b, how="left", on="userId") #-> Join all values as present in left table
product_transactions = pd.merge(transactions,product_areas, how="outer", on="product_area_id")

#right ---->
pd.merge(df_a,df_b, how="right", on="userId") #-> Join all values as present in right table

#outer ---->
pd.merge(df_a,df_b, how="outer", on="userId") #-> Join all values as both table and replaces null values

#join multiple coulumns
pd.merge(df_a,df_b, how="right", on=["userId", "Age"])

