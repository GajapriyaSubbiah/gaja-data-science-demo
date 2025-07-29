# -*- coding: utf-8 -*-
"""
Created on Tue Jul 29 11:52:49 2025

@author: subbi
"""

import matplotlib.pyplot as plt

import pandas as pd

body_data = pd.read_csv("weights_and_heights.csv")

male = body_data[body_data["Gender"] == "Male"]
female = body_data[body_data["Gender"] == "Female"]

male_sample = male.sample(200, random_state = 42)

plt.style.use('ggplot')
plt.scatter(male_sample["Weight"], male_sample["Height"], color="blue", s=700, alpha=0.5)
plt.title("Weight vs Weight")
plt.xlabel("Weight")
plt.ylabel("Height")
plt.axvline(x = male_sample["Weight"].median(), color="black", linestyle="--")
plt.axhline(y = male_sample["Height"].median(), color="black", linestyle="--")
plt.tight_layout()
plt.show()