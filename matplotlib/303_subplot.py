# -*- coding: utf-8 -*-
"""
Created on Wed Jul 23 12:49:01 2025

@author: subbi
"""

import matplotlib.pyplot as plt

x_values = [1,2,3,4,5,6,7,8,9,10]
x_squared = [x **2 for x in x_values]
x_cubed = [x **2 for x in x_values]

#subplot as horizontal
plt.subplot(2,1,1)

plt.plot(x_values,x_squared, label="The values of X")
plt.xlabel("X")
plt.ylabel("squared")
plt.title("The exponential growth")


plt.subplot(2,1,2)

plt.plot(x_values,x_cubed, label="The values of X")
plt.xlabel("X")
plt.ylabel("cubed")
plt.title("The exponential growth")
plt.tight_layout()
plt.show()

#subplot as vertical
plt.subplot(2,2,1)

plt.plot(x_values,x_squared, label="The values of X")
plt.title("squared")
plt.xlabel("X")
plt.ylabel("squared")



plt.subplot(2,2,2)

plt.plot(x_values,x_cubed, label="The values of X")
plt.title("The exponential growth")
plt.xlabel("X")
plt.ylabel("cubed")


plt.subplot(2,2,3)

plt.plot(x_values,x_squared, label="The values of X")
plt.title("The exponential growth")
plt.xlabel("X")
plt.ylabel("squared")



plt.subplot(2,2,4)

plt.plot(x_values,x_cubed, label="The values of X")
plt.title("The exponential growth")
plt.xlabel("X")
plt.ylabel("cubed")


plt.tight_layout()
plt.show()