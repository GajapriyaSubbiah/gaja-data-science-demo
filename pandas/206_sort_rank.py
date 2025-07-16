# -*- coding: utf-8 -*-
"""
Created on Wed Jul 16 15:40:42 2025

@author: subbi
"""

import pandas as pd

customer_details = pd.read_excel("grocery_database.xlsx", sheet_name="customer_details")

#sort

customer_details.sort_values(by = "distance_from_store", inplace=True)
customer_details.sort_values(by = ["distance_from_store", "credit_score"], inplace=True)
customer_details.sort_values(by = ["distance_from_store", "credit_score"], ascending=False, inplace=True)
customer_details.sort_values(by = ["distance_from_store", "credit_score"], ascending=False, inplace=True, na_position="first")



#Rank
import numpy as np
x = pd.DataFrame({"A": [1, 1, 2, 3, 5, 6, 7, 8, np.nan, 9]})
x.sort_values(by = ["A"], inplace=True, ascending=True)
x["A"].rank()
x["col2"] = x["A"].rank()

x["avg"] = x["A"].rank(method="average") #normal ranking from order
x["min"] = x["A"].rank(method="min")
x["max"] = x["A"].rank(method="max")
x["firstrank"] = x["A"].rank(method="first")
x["dense"] = x["A"].rank(method="dense") # will skip the value in order if we have same values

x["dense_na_top"] = x["A"].rank(method="dense", na_option="top")
x["dense_na_bottom"] = x["A"].rank(method="dense", na_option="bottom")