"""Fixed Point Method."""


def fixed_point(function, x0, iteration):
    """Here is the code of the method."""
    for cycle in range(iteration):
        x0 = function(x0)
    return x0


def function(x):
    """Here you gonna code the function you want to evaluate."""
    pass


def original_function(x):
    """Here you gonna code the function you want to evaluate."""
    pass
