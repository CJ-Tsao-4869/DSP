# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 14:28:54 2026

This file demonstrates how to produce a cosine wave and show it on the screen.

@author: georg
"""

import numpy as np
import matplotlib.pyplot as plt

# t : Define an array to store the time samples
# s : Define an array to store the values according to the time samples
t = np.linspace(0, 1, 1000, endpoint=False)
x = np.cos(2*np.pi*5*t)

plt.plot(t, x)              # plot(x_axis, y_axis)
plt.xlabel('t (second)')    # Name of x axis
plt.ylabel('Amplitude')     # Name of y axis
plt.show()                  # show the plot on the screen