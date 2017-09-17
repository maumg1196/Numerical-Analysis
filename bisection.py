"""Bisection Method."""


def samesign(a, b):
    return a * b > 0


def bisect(func, low, high, iteration):
    """Find root of continuous function where
    f(low) and f(high) have opposite signs."""

    assert not samesign(func(low), func(high))

    for i in range(iteration):
        midpoint = (low + high) / 2.0
        if samesign(func(low), func(midpoint)):
            low = midpoint
        else:
            high = midpoint

    return midpoint


def function(x):
    # You can put the function you one here
    return x**3


print('\t\tBISECTION METHOD\n\n')
iteration = int(input('Enter de number of cycles you want to do the method: '))
low = int(input('Enter the low number: '))
high = int(input('Enter the high number: '))
x = bisect(function, low, high, iteration)
print(x, function(x))
