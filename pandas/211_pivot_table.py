# -*- coding: utf-8 -*-
"""
Created on Mon Jul 21 12:35:53 2025

@author: subbi
"""

import pandas as pd

transactions = pd.read_excel("grocery_database.xlsx", sheet_name="transactions")

product_areas = pd.read_excel("grocery_database.xlsx", sheet_name="product_areas")

#merge two tables

transactions = pd.merge(transactions, product_areas, how="inner", on="product_area_id")

transactions.groupby("product_area_name")["sales_cost"].sum().reset_index()


#instead of agregating the data we can do pivot table

sales_summary = transactions.pivot_table(index="transaction_date",
                               columns="product_area_name",
                               values="sales_cost",
                               aggfunc="sum")

#some extra parameter
"""
fill_value is used to fill null values,
margin = sum of rows
"""
sales_summary = transactions.pivot_table(index=["transaction_date","product_area_id"],
                               columns="product_area_name",
                               values="sales_cost",
                               aggfunc="sum",
                               fill_value=0,
                               margins=True,
                               margins_name="Total")