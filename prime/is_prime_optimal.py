import math


def is_prime(n: int) -> bool:
    """Decide the whether the given interger is prim number or not more efficiently

    >>> is_prime(1)
    False
    >>> is_prime(2)
    True
    >>> is_prime(877)
    True
    >>> is_prime(10003002003)
    False
    >>> is_prime(32416190071)
    True
    >>> is_prime(-37)
    Traceback (most recent call last):
        ...
    ValueError: n must be >= 1
    >>> is_prime(36.5)
    Traceback (most recent call last):
        ...
    ValueError: n must be exact integer
    """
    if n < 1:
        raise ValueError("n must be >= 1")
    if math.floor(n) != n:
        raise ValueError("n must be exact integer")
    if n == 1:
        return False
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True
