# -*- coding: utf-8 -*-
"""
Created on Thu Jul 10 12:27:56 2025

@author: subbi
"""

import pandas as pd

transactions = pd.read_excel("grocery_database.xlsx", sheet_name="transactions")

transactions["store_id"] = 1

transactions["profit"] = transactions["sales_cost"] * 5

import numpy as np

transactions["sales_type"] = np.where(transactions["profit"] > 50, "Large", "Small")

condition_rule = [transactions["profit"] > 100, transactions["profit"] > 35, transactions["profit"] < 35]
outcomes = ["Large", "medium", "small"]

transactions["sales_type"] = np.select(condition_rule, outcomes, default="x-small")

new_df = transactions.drop(["store_id"], axis=1)