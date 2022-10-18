import math

x = float(input('x=')) #D = (-7; 9)
R = float(input('R=')) #R = (-3; R2)

if x <= -5:
    y = -3
elif x > -5 and x <= -R:
    y = 1.5*(x+3)
elif x > -R and x <= R:
    R2 = math.pow(R, 2)
    X2 = math.pow(x, 2)
    y = math.sqrt(R2-X2)
elif x > R and x <= 8:
    y = (x-3)/2.5
elif x > 8:
    y = R
else:
    y = 'Число не входить в область визначення'

print('y=', round(y, 1))