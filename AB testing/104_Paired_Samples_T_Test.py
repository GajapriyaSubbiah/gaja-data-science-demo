# -*- coding: utf-8 -*-
"""
Created on Thu Jul 31 12:26:19 2025

@author: subbi
"""

#import the required packages
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import ttest_rel, norm

#as this is an independent samples t test we need two samples
before = norm.rvs(loc=500, scale=100, size=100, random_state=42).astype(int)

np.random.seed(42)
after = before + np.random.randint(low=-50, high=75, size=100)

#plot the samples
plt.hist(before, density=True, alpha=0.5)
plt.hist(after, density=True, alpha=0.5)
plt.show()

#print the mean of the two samples data
before_mean = before.mean()
after_mean = after.mean()
print(before_mean, after_mean)

#set the hypothesis and acceptance criteria
null_hypothesis = "The mean of the before_mean is equal to the mean of the after_mean"
alternate_hypothesis = "The mean of the before_mean is different to the mean of after_mean"
acceptance_criteria = 0.05

#execute the hypothesis
t_statistic, p_value = ttest_rel(before, after)
print(t_statistic, p_value)

#print the hypothesis and p-value
if p_value <= acceptance_criteria:
    print(f"The mean of the sample p value {p_value} is lower than acceptance criteria {acceptance_criteria}. Hence we reject the null hypothesis. {alternate_hypothesis}")
else:
    print(f"The mean of the sample p value {p_value} is higher than acceptance criteria {acceptance_criteria}. Hence we retain the null hypothesis. {null_hypothesis}")