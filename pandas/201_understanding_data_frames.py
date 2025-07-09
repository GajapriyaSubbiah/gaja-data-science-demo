# -*- coding: utf-8 -*-
"""
Created on Wed Jul  9 16:14:10 2025

@author: subbi
"""

import pandas as pd

transactions = pd.read_excel("grocery_database.xlsx", sheet_name="transactions")

transactions.shape
transactions.describe()
transactions.head(5)
transactions.tail(5)
transactions.sample(5)

sample = transactions.sample(frac=0.1)

transactions.isna()


customer_details = pd.read_excel("grocery_database.xlsx", sheet_name="customer_details")

customer_details.describe()
customer_details.isna().sum()

customer_details.nlargest(25, "distance_from_store")
customer_details.nsmallest(25, "distance_from_store")
customer_details.nunique()
