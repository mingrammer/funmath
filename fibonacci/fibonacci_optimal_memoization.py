fibo_dict = {
    0: 0,
    1: 1,
}


def fibonacci_optimal_memoization(n: int) -> int:
    """Return the nth fibonacci number using optimal memoization method

    This function uses fibonacci dict for caching the calculated fibonacci numbers.
    So it does not recalculate the every fibonacci number, so this would be very fast.

    >>> fibonacci_optimal_memoization(0)
    0
    >>> fibonacci_optimal_memoization(1)
    1
    >>> fibonacci_optimal_memoization(50)
    12586269025
    >>> fibonacci_optimal_memoization(200)
    280571172992510140037611932413038677189525
    >>> fibonacci_optimal_memoization(-2)
    Traceback (most recent call last):
        ...
    ValueError: n must be >= 0
    """
    if n < 0:
        raise ValueError("n must be >= 0")
    if n in fibo_dict:
        return fibo_dict[n]
    else:
        fibo_dict[n] = fibonacci_optimal_memoization(n - 1) + fibonacci_optimal_memoization(n - 2)
        return fibo_dict[n]
