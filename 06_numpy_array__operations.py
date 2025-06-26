# -*- coding: utf-8 -*-
"""
Created on Thu Jun 26 12:53:33 2025

@author: subbi
"""

import numpy as np

#to create random integers between 2 and 8 = 16 numbers in total
my_1d_array = np.random.randint(2,8,16)

#to perform min, max, mean, squre, sqrt, std

print("max:", my_1d_array.max())
print("min:", my_1d_array.min())
print("mean:", my_1d_array.mean())
print("std:", my_1d_array.std())
print("square:", np.square(my_1d_array))
print("square root:", np.sqrt(my_1d_array))


# to shape from 1 d to 2d array
my_2d_array = my_1d_array.reshape(4,4)

# to check the max or min value in col wise use axis = 0
my_2d_array.max(axis=0)

# axis = 1 for row wise
my_2d_array.max(axis=1)

#to find index of that position of max - coluumn numbers
my_2d_array.argmax(axis=0)

#to find index of that position of max - row numbers
my_2d_array.argmax(axis=1)

np.sort(my_1d_array)

a=np.array([1,2,3,4,5])
b=np.array([6,7,8,9,10])
# we can perform arithmetic operations like this
a + b

# to find the dot product (1*6)+(2*7).....
print("dot:", np.dot(a,b))