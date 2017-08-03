def next_prime(n: int) -> int:
    """Find the next prime after the input

    >>> next_prime(3)
    5
    >>> next_prime(1421)
    1423
    >>> next_prime(-26)
    Traceback (most recent call last):
        ...
    ValueError: n must be >= 1
    >>> next_prime(80023045)
    80023051
    """
    if n <= 0:
        raise ValueError("n must be >= 1")
    n += 1
    for p in range(n, 2 * n):
        for i in range(2, p):
            if p % i == 0:
                break
        else:
            return p
