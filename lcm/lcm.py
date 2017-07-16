def lcm(a: int, b: int) -> int:
    """Return a LCM (Lowest Common Multiple) of given two integers

    >>> lcm(3, 10)
    30
    >>> lcm(42, 63)
    126
    >>> lcm(40, 80)
    80
    >>> lcm(-20, 30)
    60
    """
    g = min(abs(a), abs(b))
    while g >= 1:
        if a % g == 0 and b % g == 0:
            break
        g -= 1
    return abs(int((a * b) / g))
