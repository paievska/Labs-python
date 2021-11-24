from numpy import* 
import math
import matplotlib.pyplot as plt 
 
def f1(t): 
    return 10 * (math.cos(t**2)/(t**2) )
t = linspace(0, 4) 
y = f1(t) 
 
t = linspace(0, 4) 
plt.plot(t, y, 'g-', label = '10*cos(x^2)/x^2', color = "pink") 
plt.axis([0, 4, -5, 5])  
plt.grid() 
plt.xlabel('t') 
plt.xlabel('y') 
plt.title('10*cos(x^2)/x^2') 
plt.legend() 
plt.show()