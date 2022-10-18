import math

a = int(input('a='))
3
b = int(input('b='))
c = int(input('c='))
x = int(input('x='))

if c < 0 and b != 0:
    F = a*x^2+b
elif x > 0 and b ==0:
    F = (x-a)/(x-c)
else:
    F = x/c

print(F)