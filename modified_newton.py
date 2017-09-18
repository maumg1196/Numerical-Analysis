"""Modified Newton Raphson Method."""
from sympy import *


def modified_newton(function, x0, iteration):
    """Here is the code of all the method."""
    prime = diff(function)
    biprime = diff(prime)
    print(biprime)
    for cycle in range(iteration):
        x0 -= ((function.evalf(subs={x: x0}) * prime.evalf(subs={x: x0})) / (prime.evalf(subs={x: x0})**2 - function.evalf(subs={x: x0}) * biprime.evalf(subs={x: x0})))
    return x0


x = Symbol('x')
