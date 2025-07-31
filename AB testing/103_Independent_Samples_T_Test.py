# -*- coding: utf-8 -*-
"""
Created on Thu Jul 31 12:10:31 2025

@author: subbi
"""

#import the required packages
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind, norm

#as this is an independent samples t test we need two samples
sample_A = norm.rvs(loc=500, scale=100, size=250, random_state=42).astype(int)

sample_B = norm.rvs(loc=550, scale=150, size=100, random_state=42).astype(int)

#plot the samples
plt.hist(sample_A, density=True, alpha=0.5)
plt.hist(sample_B, density=True, alpha=0.5)
plt.show()

#print the mean of the two samples data
sample_A_mean = sample_A.mean()
sample_B_mean = sample_B.mean()
print(sample_A_mean, sample_B_mean)

#set the hypothesis and acceptance criteria
null_hypothesis = "The mean of the sample A is equal to the mean of the sample B"
alternate_hypothesis = "The mean of the sample A is different to the mean of the sample B"
acceptance_criteria = 0.05

#execute the hypothesis
t_statistic, p_value = ttest_ind(sample_A, sample_B)
print(t_statistic, p_value)

#print the hypothesis and p-value
if p_value <= acceptance_criteria:
    print(f"The mean of the sample p value {p_value} is lower than acceptance criteria {acceptance_criteria}. Hence we reject the null hypothesis. {alternate_hypothesis}")
else:
    print(f"The mean of the sample p value {p_value} is higher than acceptance criteria {acceptance_criteria}. Hence we retain the null hypothesis. {null_hypothesis}")