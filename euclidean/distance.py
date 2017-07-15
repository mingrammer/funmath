import math
from typing import Tuple


def euclidean_distance(p1: Tuple[float, float], p2: Tuple[float, float]) -> float:
    """Calculate the distance between two points on coordinate plane

    >>> euclidean_distance((0, 0), (3, 4))
    5.0
    >>> euclidean_distance((-1, 3), (7, 9))
    10.0
    """
    x1, y1 = p1
    x2, y2 = p2
    dx = x1 - x2
    dy = y1 - y2
    return math.sqrt(dx ** 2 + dy ** 2)
