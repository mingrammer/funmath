import math


def abs(x):
    """Return the absolute value of x, a numeric value
    
    >>> abs(3)
    3
    >>> abs(-10)
    10
    >>> abs(0)
    0
    >>> abs(-3.14)
    3.14
    >>> abs(-3 + 4j)
    5.0
    """
    if isinstance(x, complex):
        return math.sqrt(x.real ** 2 + x.imag ** 2)
    return x if x >= 0 else -x
