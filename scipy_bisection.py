import scipy.optimize as optimize


def function(x):
    return x**3


print(optimize.bisect(function, -3, 5))
