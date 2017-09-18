"""Taylor's Polynomial."""
from sympy import *


def taylor(function, x0, initial, iteration):
    """Here is all the code of the method."""
    total = 0
    for cycle in range(iteration):
        if cycle == 0:
            total += function.evalf(subs={x: x0})
        else:
            function = diff(function)
            first = function / factorial(cycle)
            second = initial - x0
            total += first * second
    return total


x = Symbol('x')
