import math

x1=3.74
x2=3.77

xx1=math.sqrt(14)
xx2=49/13

dx1=xx1-x1
dx2=xx2-x2

if dx2>dx1:
    print("Нерівність",x1,"точніша")
else:
    print("Нерівність",x2,"точніша")