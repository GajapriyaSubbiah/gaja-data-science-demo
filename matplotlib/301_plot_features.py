# -*- coding: utf-8 -*-
"""
Created on Tue Jul 22 13:40:18 2025

@author: subbi
"""

import matplotlib.pyplot as plt

x_values = [1,2,3,4,5,6,7,8,9,10]
x_squared = [x ** 2 for x in x_values]
x_cubed = [x ** 3 for x in x_values]

plt.plot(x_values, x_squared, label="xvalues_squared")
plt.plot(x_values, x_cubed, label="xvalues_cubed")
plt.title("The Plot features")
plt.xlabel("The values of X")
plt.ylabel("The values of Y")
plt.grid(True)
plt.legend()
plt.show()

