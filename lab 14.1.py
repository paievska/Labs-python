import math
import numpy as np
from numpy import *
import matplotlib.pyplot as plt
#Variant 17 - Method Euler-Cauchy
def f(x,y):
    p=x+math.cos(y/math.sqrt(11))
    return p
x0=2.1
ux=3.1
h=0.1
x=np.arange(x0,ux+h,h)
n=len(x)-1
y=np.empty(n+1)
y[0]=2.5
for i in range(n):
    y[i+1]=y[i]+(f(x[i],y[i])+f(x[i+1],y[i]+h*f(x[i],y[i])))*h/2
y_rounded=np.round_(y,4)
print('x=',x)
print('y=',y_rounded)
plt.plot(x, y,'o',x,y,'g-')
plt.xlabel('x') 
plt.ylabel('y')
plt.title('Метод Ейлера-Коші') 
plt.legend(['точки','x+cos(y/√11)'])
plt.grid()
plt.show()