def is_prime(n: int) -> bool:
    """Decide the whether the given integer is prime number or not

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
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
