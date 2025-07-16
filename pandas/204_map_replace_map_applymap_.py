# -*- coding: utf-8 -*-
"""
Created on Wed Jul 16 12:10:02 2025

@author: subbi
"""

import pandas as pd

customer_details = pd.read_excel("grocery_database.xlsx", sheet_name="customer_details")

#Map

customer_details["gender_updated"] = customer_details["gender"].map({"M": 1,
                                                                     "F": 0})

customer_details["gender_updated"] = customer_details["gender"].map({"M": 1})

#if we didnt specify any values then it will nan - null, but replace retain the original values


#Replace
pd.set_option('future.no_silent_downcasting', True)
customer_details["gender_updated"] = customer_details["gender"].replace({"M": 1}).infer_objects(copy=False)

#apply
product_areas = pd.read_excel("grocery_database.xlsx", sheet_name="product_areas")

def updated_profit_margin(profit_margin):
    if profit_margin > 0.5:
        return profit_margin ** 0.8
    else:
        return profit_margin ** 0.2
    

product_areas["profit_margin_updated"] = product_areas["profit_margin"].apply(updated_profit_margin)


#applymap

df = pd.DataFrame({"A": [1,2,3],
                   "B": [1,2,3],
                   "C": [1,2,3]})

def square(n):
    return n **2

df = df.applymap(square)