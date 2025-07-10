# -*- coding: utf-8 -*-
"""
Created on Thu Jul 10 12:08:20 2025

@author: subbi
"""

import pandas as pd

my_data = pd.read_excel("grocery_database.xlsx", sheet_name="transactions")

my_data_colums = my_data[["customer_id", "sales_cost"]]