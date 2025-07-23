# -*- coding: utf-8 -*-
"""
Created on Wed Jul 23 12:11:37 2025

@author: subbi
"""

import matplotlib.pyplot as plt

x_values = [1,2,3,4,5,6,7,8,9,10]
x_squared = [x ** 2 for x in x_values]
x_cubed = [x ** 3 for x in x_values]

plt.style.available
plt.style.use('ggplot')

plt.plot(x_values, x_squared, label="The x2 values of x",  marker='o', linestyle='--', linewidth=3, markersize=8, color='green', markeredgecolor='green', markerfacecolor ='red')
plt.plot(x_values, x_cubed, label="The x3 values of x", marker='*', linestyle='--', linewidth=3, markersize=14, color='red', markeredgecolor='red', markerfacecolor ='blue')
plt.title("The exponential growth")
plt.legend()
plt.show()
