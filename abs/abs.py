from typing import Union


def abs(x: Union[int, float]) -> Union[int, float]:
    """Return the absolute value of x, a real number
    
    >>> abs(3)
    3
    >>> abs(-10)
    10
    >>> abs(0)
    0
    >>> abs(-3.14)
    3.14
    """
    return x if x >= 0 else -x
