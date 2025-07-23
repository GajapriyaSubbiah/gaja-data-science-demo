# -*- coding: utf-8 -*-
"""
Created on Wed Jul 23 14:32:18 2025

@author: subbi
"""

import matplotlib.pyplot as plt
import pandas as pd
body_data=pd.read_csv("weights_and_heights.csv")

male = body_data[body_data["Gender"]=="Male"]
female = body_data[body_data["Gender"]=="Female"]
plt.hist(male["Weight"], bins=20, label="Male", color="pink", alpha=0.6, edgecolor="black")
plt.hist(female["Weight"], bins=20, label="female", color="blue", alpha=0.6, edgecolor="black")
plt.title("The weight of male and female")
plt.xlabel("Weight")
plt.xlabel("Frequency")
plt.legend()
plt.tight_layout()
plt.show()
