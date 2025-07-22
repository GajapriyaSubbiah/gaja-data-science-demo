# -*- coding: utf-8 -*-
"""
Created on Mon Jul 21 21:58:39 2025

@author: subbi
"""

import pandas as pd

customer_details = pd.read_excel("grocery_database.xlsx", sheet_name="customer_details")

customer_details.isna().sum()

customer_details.notna().sum()

customer_details["distance_from_store"].isna().sum()

customer_details[customer_details["distance_from_store"].notna()]

customer_details.dropna(how = "any")
customer_details.dropna(how = "all")

customer_details.dropna(how = "any", subset = ["distance_from_store"])

customer_details.dropna(how = "any", subset = ["distance_from_store", "gender"])

import numpy as np

my_df = pd.DataFrame({"A": [1,2,3,np.nan,5,6],
                      "B": [1,2,3,np.nan,5,np.nan]})

my_df["A"].fillna(value=0)

impertiva_value = my_df["A"].mean()

my_df["A"].fillna(value=impertiva_value)