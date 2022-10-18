import math

x = float(input('x='))
ex = 5*math.pow(math.e, 3*x)

if x <= -1:
    y = ex - (3+math.sin(math.fabs(x)))
elif -1<x and x<3:
    y = ex - (2*math.pow(math.e, x/4-1))
else:
    y = ex - (7-math.sqrt(2*math.pow(x, 3)))
print(y)