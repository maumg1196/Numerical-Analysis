"""Newtwon Raphson Method."""
from sympy import *


def nwrph(function, prime, x0, iteration):
    """Here is the Newton Raphson Method."""
    for loop in range(iteration):
        x0 = x0 - (function.evalf(subs={x: x0}) / prime.evalf(subs={x: x0}))
    return x0


x = Symbol('x')

# Here you gonna write the function you want
function = exp(-x) - x
fprime = diff(function)
x0 = int(input('Enter x0'))
iteration = int(input('Enter the number of cycles'))
newton = nwrph(function, fprime, x0, iteration)
print(newton)
