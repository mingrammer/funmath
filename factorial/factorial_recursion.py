def factorial(n: int) -> int:
    """Return the factorial of n, an exact integer >= 0

    By definition, the factorial is defined as follow:
    factorial(n) = n * factorial(n - 1), factorial(0) = factorial(1) = 1

    >>> factorial(4)
    24
    >>> factorial(10)
    3628800
    >>> factorial(25)
    15511210043330985984000000
    >>> factorial(-2)
    Traceback (most recent call last):
        ...
    ValueError: n must be >= 0
    """
    if n < 0:
        raise ValueError("n must be >= 0")
    if n <= 1:
        return 1
    return n * factorial(n - 1)
