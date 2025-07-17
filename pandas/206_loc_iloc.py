# -*- coding: utf-8 -*-
"""
Created on Thu Jul 17 13:34:41 2025

@author: subbi
"""

import pandas as pd
customer_details = pd.read_excel("grocery_database.xlsx", sheet_name="customer_details")

#iloc

customer_details.iloc[89]
customer_details.iloc[0:3, :]
customer_details.iloc[:, [0,2,-1]]

#loc
customer_details.loc[0]
customer_details.set_index("customer_id", inplace=True)
customer_details.reset_index(inplace=True)

customer_details.loc[0:3, ["customer_id", "credit_score"]]

customer_details.loc[customer_details["customer_id"] == 74]

customer_details.loc[
    (customer_details["customer_id"] == 74) | (customer_details["customer_id"] == 100 )]

customer_details.loc[customer_details["customer_id"].isin([74,100])]
customer_details.loc[~customer_details["customer_id"].isin([74,100])]