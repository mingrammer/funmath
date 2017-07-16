def fibonacci_optimal_iteration(n: int) -> int:
    """Return the nth fibonacci number using optimal iteration method

    This function calculate a fibonacci number using iteration loop, not recursion.
    So it has O(n) time complexity which is very fast.

    >>> fibonacci_optimal_iteration(0)
    0
    >>> fibonacci_optimal_iteration(1)
    1
    >>> fibonacci_optimal_iteration(50)
    12586269025
    >>> fibonacci_optimal_iteration(200)
    280571172992510140037611932413038677189525
    >>> fibonacci_optimal_iteration(-2)
    Traceback (most recent call last):
        ...
    ValueError: n must be >= 0
    """
    if n < 0:
        raise ValueError("n must be >= 0")
    a, b = 0, 1
    for _ in range(1, n + 1):
        a, b = b, a + b
    return a
