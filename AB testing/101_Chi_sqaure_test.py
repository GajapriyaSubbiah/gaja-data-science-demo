# -*- coding: utf-8 -*-
"""
Created on Wed Jul 30 14:45:48 2025

@author: subbi
"""

#import required packages
import pandas as pd
from scipy.stats import chi2_contingency, chi2

#read the file
campaign_data = pd.read_excel("grocery_database.xlsx", sheet_name="campaign_data")

#filter the data using loc function
campaign_data = campaign_data[campaign_data["mailer_type"] != "Control"]

#observed freqencies to need for chi squared t test
observed_values = pd.crosstab(campaign_data["mailer_type"], campaign_data["signup_flag"]).values

mailer1_signup = 123 / (252+123)
mailer2_signup = 127 / (209+127)
print(mailer1_signup, mailer2_signup)

#set variables for null and alternate hypothesis
null_hypothesis = "There is no relationship between mailer type and signup rate. They are independent"
alternate_hypothesis = "There is a relationship between mailer type and signup rate. They are not independent"
acceptance_criteria = 0.05

#calculate the expected freq and chi-squared statistics
chi2_statistic, p_value, dof, expected_values = chi2_contingency(observed_values, correction=False)
print(chi2_statistic, p_value)

#to find the critical value
#ppf is a percentage point function - find out critical value along with the chi-squared distribution based on 
#the accpetance criteria
critical_value = chi2.ppf(1- acceptance_criteria, dof)
print(critical_value)

#print the results
if chi2_statistic >= critical_value:
    print(f"As our chi-squared statistics is higher than the critical value {critical_value}. Since we can reject the null hypothesis. {alternate_hypothesis}")
else:
    print(f"As our chi-squared statistics is lower than the critical value {critical_value}. Since we can retain the null hypothesis. {null_hypothesis}")
    
#print the results based on the p value
if p_value <= acceptance_criteria:
    print(f"As our p_value is lower than the critical value {acceptance_criteria}. Since we can reject the null hypothesis. {alternate_hypothesis}")
else:
    print(f"As our p_value is higher than the critical value {acceptance_criteria}. Since we can retain the null hypothesis. {null_hypothesis}")
    
