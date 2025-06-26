# -*- coding: utf-8 -*-
"""
Created on Fri Apr 25 12:00:00 2025

@author: subbi
"""

import numpy as np

# 1d array creation
my_1d_array = np.array([1,2,3,4])
type(my_1d_array)
my_1d_array.shape

# 2d array creation
my_2d_array = np.array([
    [1,2,3],
    [4,5,6]])
type(my_2d_array)
my_2d_array.shape

#to create zero arrray
my_zero_array = np.zeros(3)

my_2d_zeroarray = np.zeros((3,3))

my_3d_zeroarray = np.zeros((4,4,4))

#to create ones array

np.ones(3)
np.ones((3,3))

#to fill the values of specified number
np.full((3,3),6)

#to get the rnage of number between two number
np.arange(3,10,1)
np.arange(1,20,2)

#to create linear space numbers between two numbers
#it will create a straight line if we plot the numbers

np.linspace(1,5,20)

#to round the values
np.round((np.linspace(1,5,20)),2)

#to find the random numbers
np.random.rand(3)

#random integers
np.random.randint(3,10,10)

#to change the 2d to 1d
my_3d_zeroarray = my_2d_zeroarray.reshape(3,3)







