# -*- coding: utf-8 -*-
"""
Created on Tue Jul 29 12:22:00 2025

@author: subbi
"""

import matplotlib.pyplot as plt
import pandas as pd

body_data = pd.read_csv("weights_and_heights.csv")

male = body_data[body_data["Gender"] == "Male"]

female = body_data[body_data["Gender"] == "Female"]

male_sample = male.sample(200, random_state = 42)
patient = male_sample.loc[[705]]
#print(plt.style.available)
plt.style.use("seaborn-v0_8")
plt.scatter(male_sample["Weight"], male_sample["Height"], color="blue", s=700, alpha=0.5)
plt.scatter(patient["Weight"], patient["Height"], color="pink", s=700)
plt.title("Weight vs Height Data")
plt.xlabel("Weight")
plt.ylabel("Height")
plt.axvline(x=male_sample["Weight"].median(), color="black", linestyle="dashdot")
plt.axhline(y=male_sample["Height"].median(), color="black", linestyle="dashdot")
plt.tight_layout()
plt.show()