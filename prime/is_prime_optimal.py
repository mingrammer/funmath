import math


def is_prime_optimal(n: int) -> bool:
    """Decide the whether the given interger is prim number or not more efficiently

    >>> is_prime_optimal(1)
    False
    >>> is_prime_optimal(2)
    True
    >>> is_prime_optimal(877)
    True
    >>> is_prime_optimal(10003002003)
    False
    >>> is_prime_optimal(32416190071)
    True
    >>> is_prime_optimal(-37)
    Traceback (most recent call last):
        ...
    ValueError: n must be >= 1
    """
    if n < 1:
        raise ValueError("n must be >= 1")
    if n == 1:
        return False
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True
