# -*- coding: utf-8 -*-
"""
Created on Thu Jul 17 14:34:48 2025

@author: subbi
"""

import pandas as pd
customer_details = pd.read_excel("grocery_database.xlsx", sheet_name="customer_details")


customer_details.rename(columns = {"customer_id":"patner_id"}, inplace=True)

customer_details.columns = customer_details.columns.str.replace(" ", "_")