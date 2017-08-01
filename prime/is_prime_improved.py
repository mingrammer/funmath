from math import sqrt


def is_prime(n: int) -> bool:
    """Decide the whether the given interger is prime number or not

    >>> is_prime(1)
    False
    >>> is_prime(2)
    True
    >>> is_prime(119)
    False
    >>> is_prime(977)
    True
    >>> is_prime(-37)
    Traceback (most recent call last):
        ...
    ValueError: n must be >= 1
    """
    if n < 1:
        raise ValueError("n must be >= 1")
    if n == 1:
        return False
    if n in (2, 3, 5):
        return True
    for i in range(6, int(sqrt(n)), 6):
        if n % (i - 1) == 0:
            return False
        if n % (i + 1) == 0:
            return False
    return True
