"""Secant Method."""


def secant(f, x0, x1, iteration):
    """Here is all the code of the method."""
    for cycle in range(iteration):
        x2 = x1 - f(x1) * ((x1 - x0) / (f(x1) - f(x0)))
        x0 = x1
        x1 = x2
    return x2


def function(x):
    """Here you gonna code the function you want to evaluate."""
    pass
