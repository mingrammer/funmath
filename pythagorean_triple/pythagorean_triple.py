from typing import List
from typing import Tuple


def pythagorean_triple(n: int) -> List[Tuple[int, int, int]]:
    """Find all pythagorean triple satisfying the following equation

    a^2 + b^2 = c^2 (1 <= a <= b <= c and a, b, c are natural numbers)

    (above 'c' is same to given 'n' parameter)

    There can be many different solutions such as (3, 4, 5), (5, 12, 13) and so on

    >>> pythagorean_triple(5)
    [(3, 4, 5)]
    >>> pythagorean_triple(14)
    [(3, 4, 5), (5, 12, 13), (6, 8, 10)]
    >>> pythagorean_triple(26)
    [(3, 4, 5), (5, 12, 13), (6, 8, 10), (7, 24, 25), (8, 15, 17), (9, 12, 15), (10, 24, 26), (12, 16, 20), (15, 20, 25)]
    >>> pythagorean_triple(1)
    Traceback (most recent call last):
        ...
    ValueError: n must be >= 2
    """
    if n < 2:
        raise ValueError('n must be >= 2')
    triple = [(a, b, c) for a in range(1, n + 1) for b in range(a, n + 1) for c in range(b, n + 1) if
              a ** 2 + b ** 2 == c ** 2]
    return triple
