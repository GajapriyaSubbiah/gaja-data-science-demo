# -*- coding: utf-8 -*-
"""
Created on Fri Jun 27 12:29:40 2025

@author: subbi
"""

#finding the volumes of the planet
#formula = V = (4/3) * π * r³

import numpy as np
radii = np.array([2439.7, 6051.8, 6371, 3389.7, 69911, 58232, 25362, 24622])

#to caluculate the radius
r = 10
volume = 4/3 * np.pi * r**3
print(volume)

#now we need to calculate for our planets
volumes = 4/3 * np.pi * radii**3
print(volumes)

#for 1 milion
radii = np.random.randint(1, 1000, 1000000)
volumes = 4/3 * np.pi * radii**3
print(volumes)