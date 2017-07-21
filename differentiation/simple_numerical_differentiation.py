from typing import Callable


def simple_numerical_differentiation(f: Callable[[float], float], x: float) -> float:
    """Calculate the differential value for given point(x) on given function(f)

    By definition, the differential value of a function is defined as follow:
    diff = [lim h go to 0] (f(x + h) - f(x - h)) / 2h

    # f(x) = 2x
    >>> abs(simple_numerical_differentiation(lambda x: 2*x, 3) - 2) < 1e-06
    True

    # f(x) = 3x^3 - 2x^2 + x - 3
    >>> abs(simple_numerical_differentiation(lambda x: 3*x**3 - 2*x**2 + x - 3, 1) - 6) < 1e-06
    True
    """
    h = 1e-4
    diff = (f(x + h) - f(x - h)) / (2 * h)
    return diff
