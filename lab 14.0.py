import math
import numpy as np
from numpy import *
import matplotlib.pyplot as plt
#Variant 17 - Method Eulera
def f(x,y):
    p=x+math.sin(y/math.e)
    return p
x0=1.4
ux=2.4
h=0.1
x=np.arange(x0,ux+h,h)
n=len(x)-1
y=np.empty(n+1)
y[0]=2.5
for i in range(n):
    y[i+1]=y[i]+f(x[i],y[i])*h
y_rounded=np.round_(y,4)
print('x=',x)
print('y=',y_rounded)
plt.plot(x, y,'o',x,y,'g-')
plt.xlabel('x') 
plt.ylabel('y')
plt.title('Метод Ейлера') 
plt.legend(['точки','x+sin(y/e)'])
plt.grid()
plt.show()


