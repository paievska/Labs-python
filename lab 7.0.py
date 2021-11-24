from numpy import *
import numpy as np
import matplotlib.pyplot as plt
import math
t = linspace(0, 4, 51)
y = 10*np.cos(t*t) / (t*t)
plt.plot(t, y, 'g--', label='10*cos(x^2)/(x^2)')
plt.axis([0, 4, -5, 10]) 
plt.legend() # вставка легенди (тексту в label)
plt.show()