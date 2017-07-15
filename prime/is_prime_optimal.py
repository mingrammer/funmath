import math
import random


RABIN_MILLER_ROUNDS = 64        # 2^-128 chance of a false positive

class ContinueOut(Exception):
    pass

def is_prime_optimal(n: int) -> bool:
    """Decide the whether the given interger is prime number or not more efficiently

    >>> is_prime_optimal(1)
    False
    >>> is_prime_optimal(2)
    True
    >>> is_prime_optimal(877)
    True
    >>> is_prime_optimal(10003002003)
    False
    >>> is_prime_optimal(32416190071)
    True
    >>> is_prime_optimal(-37)
    Traceback (most recent call last):
        ...
    ValueError: n must be >= 1
    """
    if n < 1:
        raise ValueError("n must be >= 1")
    if math.floor(n) != n:
        raise ValueError("n must be exact integer")

    if n == 1:
        return False
    elif n in [2,3,5]:            # special case where n==2, 3 or 5
        return True
    elif n%2 == 0:              # even number
        return False

    d, r = divmod(n-1, 2)       # factor out 2s from n-1
    s = 1
    while r == 0:
        s += 1
        d, r = divmod(d, 2)
    d = d*2+r
    s -= 1

    for _ in range(RABIN_MILLER_ROUNDS):
        a = random.randint(2, n-2)
        x = pow(a, d, n)
        if x == 1 or x == n-1:
            continue
        try:
            for _ in range(s-1):
                x = pow(x, 2, n)
                if x == 1:
                    return False
                if x == n-1:
                    raise ContinueOut()
        except ContinueOut:
            continue
        return False
    return True
