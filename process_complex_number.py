# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 15:05:53 2026

This file is an example of complex number.

@author: georg
"""
import numpy as np
import matplotlib.pyplot as plt

#z = 3+4j
z = complex(3, 4)
magnitude = abs(z)              # Magnitude of z
theta = np.angle(z)*180/np.pi   # Convert theta from radian to angle

print('z = ', z)
print('magnitude = ', magnitude)
print('theta = ', theta)