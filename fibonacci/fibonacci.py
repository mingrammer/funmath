def fibonacci(n: int) -> int:
    """Return the nth fibonacci number

    >>> fibonacci(0)
    0
    >>> fibonacci(1)
    1
    >>> fibonacci(10)
    55
    >>> fibonacci(20)
    6765
    >>> fibonacci(-2)
    Traceback (most recent call last):
        ...
    ValueError: n must be >= 0
    """
    if n < 0:
        raise ValueError("n must be >= 0")
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
