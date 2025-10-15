
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 11:10:22 2020, @author: jokane
"""
import sys
import matplotlib.pyplot as plt
import numpy as np
import os
os.system('cls' if os.name == 'nt' else 'clear')

print(f"Python version: {sys.version}") # viser pythonversjon 
print(f"Python path: {sys.executable}") # viser path

xstart = -10
xslutt = 10
steg = 2.0 # kurven blir glattere med kortere steg
x= np.arange(xstart, xslutt, steg)

def f(x):
    return -x**2-8*x-15
plt.plot(x,f(x))
plt.show()

''' i Spyder: 
    Figures now render in the Plots pane by default. 
    To make them also appear inline in the Console, 
    uncheck "Mute Inline Plotting" 
    under the Plots pane options menu.
'''
