def gcd(a: int, b: int) -> int:
    """Return a GCD (Greatest Common Divisor) of given two integers

    >>> gcd(1, 10)
    1
    >>> gcd(45, 81)
    9
    >>> gcd(63, 130)
    1
    >>> gcd(-20, 30)
    10
    """
    g = min(abs(a), abs(b))
    while g >= 1:
        if a % g == 0 and b % g == 0:
            return g
        g -= 1
