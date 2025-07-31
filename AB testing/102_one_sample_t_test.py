# -*- coding: utf-8 -*-
"""
Created on Thu Jul 31 11:48:36 2025

@author: subbi
"""

#import the required packages
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import ttest_1samp, norm

#mock data, distribution of credit score rvs is create random variables in form of normalization
population = norm.rvs(loc = 500, scale = 100, size = 1000, random_state = 42).astype(int)

#sample data
np.random.seed(42)
sample = np.random.choice(population, 250)


#to check the plot b/t population and sample
plt.hist(population, density=True, alpha=0.5)
plt.hist(sample, density=True, alpha=0.5)
plt.show()

population_mean=population.mean()
sample_mean = sample.mean()
print(population_mean, sample_mean)

#set the hypothesis and acceptance criteria
null_hypothesis = "The mean of the mean of the sample is equal to the mean of the population"
alternate_hypothesis = "The mean of the sample is different to the mean of the population"
acceptance_criteria = 0.05

#execute the hypothesis test
t_statistic, p_value = ttest_1samp(sample, population_mean)
print(t_statistic, p_value) 

#print the hypothesis and p - value
if p_value <= acceptance_criteria:
    print(f"The mean of the sample p value {p_value} is lower to the mean of the population. Hence we reject the null hypothesis. {alternate_hypothesis}")
else:
    print(f"The mean of the sample p value {p_value} is higher to the mean of the population. Hence we retain the null hypothesis. {null_hypothesis}")