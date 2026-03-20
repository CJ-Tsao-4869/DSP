# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 12:16:32 2026

This file demontrates how to draw digital signals using matplotlib

@author: georg
"""
import numpy as np
import matplotlib.pyplot as plt

'''
define data set
'''
n = np.array([0,1,2,3,4,5,6,7,8])
x = np.array([0,0,1,2,4,3,2,1,0])

'''
use stem to draw a discrete digital signal
'''
plt.stem(n, x)
plt.xlabel('n')
plt.ylabel('x[n]')
plt.show()
