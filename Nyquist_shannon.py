# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 11:30:41 2026

This file demonstrates the concept of sampling and Nyquist-Shannon sampling theorem.

@author: georg
"""
import numpy as np
import matplotlib.pyplot as plt

'''
sampling can be defined as x[n] = x(nTs) = x(n/fs)
where Ts represents sampling period (sampling interval), 
and fs stands for sampling frequency (sampling rate)
'''
startSeconds = 0
endSeconds = 1
fs_1 = 10000
fs_2 = 4

'''
Then we generate a array of all wanted sampling position, 
and then sampling the cosine wave which have frequency f = 10
'''
f = 10
t_1 = np.linspace(startSeconds, endSeconds, fs_1*(endSeconds-startSeconds), endpoint=False)
x_1 = np.cos(2*np.pi*f*t_1)
t_2 = np.linspace(startSeconds, endSeconds, fs_2*(endSeconds-startSeconds), endpoint=False)
x_2 = np.cos(2*np.pi*f*t_2)

'''
Try to plot the wave with fs_1 and fs_2, 
and verify the Nyquist shannon sampling theorem (fs>2f)
'''

plt.plot(t_1, x_1)      # better quality
plt.plot(t_2, x_2)      # lose informations, aliasing occur

plt.show()

