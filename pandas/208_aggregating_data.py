# -*- coding: utf-8 -*-
"""
Created on Mon Jul 21 11:57:29 2025

@author: subbi
"""

import pandas as pd

transactions = pd.read_excel("grocery_database.xlsx", sheet_name="transactions")

product_areas = pd.read_excel("grocery_database.xlsx", sheet_name="product_areas")

#merge two tables

sales_summary = pd.merge(transactions, product_areas, how="inner", on="product_area_id")

#to check the sum of the sales_cost

sales_summary.groupby("product_area_name")["sales_cost"].sum()

sales_summary.groupby(["product_area_name","num_items"])["sales_cost"].sum()

sales_summary.groupby("product_area_name")["sales_cost"].quantile([0.25, 0.50, 0.75])


#reset_index is used for DataFrame
sales_summary_merge = sales_summary.groupby("product_area_name")["sales_cost"].sum().reset_index()

#multiple columns
sales_summary_merge = sales_summary.groupby(["product_area_name", "transaction_date"])["sales_cost"].sum().reset_index()

sales_summary_merge = sales_summary.groupby(["product_area_name", "transaction_date"])[["sales_cost", "num_items"]].sum().reset_index()

#for agg
sales_summary_merge = sales_summary.groupby(["product_area_name", "transaction_date"])["sales_cost"].agg("sum").reset_index()


#for agg for multiple columns as key value pair as dictionaries
sales_summary_merge = sales_summary.groupby(["product_area_name", "transaction_date"]).agg({"sales_cost":"sum","num_items":"mean"}).reset_index()

