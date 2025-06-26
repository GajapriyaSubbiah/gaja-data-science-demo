# -*- coding: utf-8 -*-
"""
Created on Thu Jun 26 15:34:45 2025

@author: subbi
"""
import numpy as np

oned_array = np.zeros(10)
oned_array[0] = 50
oned_array[3:6] = 50
print(oned_array)

np.where(oned_array == 50)

#to check the arithemtic operatiosn like > < >= <=
#argwhere is the index of the elements based on the condition

np.where(oned_array >= 50)
np.argwhere(oned_array == 50)


#all of the elements if we didnt specify argument it wll check non -zero
np.all(oned_array == 50)
np.all(oned_array)

#any of the elements
np.any(oned_array == 50)
np.any(oned_array)

#stack together vertically or horizontally

a = np.array([[1,2],
             [3,4]])
b = np.array([[1,2],
             [3,4]])

v=np.vstack((a,b))
print(v)


h=np.hstack((a,b))
print(h)

#to reshpae the 2d to 1d is flatten
a.flatten()