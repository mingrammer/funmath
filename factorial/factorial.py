import math


def factorial(n):
    """Return the factorial of n, an exact integer >= 0

    >>> factorial(4)
    24
    >>> factorial(10.0)
    3628800
    >>> factorial(25)
    15511210043330985984000000
    >>> factorial(-2)
    Traceback (most recent call last):
        ...
    ValueError: n must be >= 0
    >>> factorial(20.2)
    Traceback (most recent call last):
        ...
    ValueError: n must be exact integer
    """
    if n < 0:
        raise ValueError("n must be >= 0")
    if math.floor(n) != n:
        raise ValueError("n must be exact integer")
    result = 1
    factor = 2
    while factor <= n:
        result *= factor
        factor += 1
    return result
