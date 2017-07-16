def gcd_optimal_euclidean(a: int, b: int) -> int:
    """Return a GCD (Greatest Common Divisor) of given two integers using euclidean algorithm

    This function uses euclidean algorithm to get GCD of two integers.
    This algorithm works as follows.

    gcd(100, 36)
    = gcd(36, 28 (= 100 mod 36))
    = gcd(28, 8 (= 36 mod 28))
    = gcd(8, 4 (= 28 mod 8))
    = gcd(4, 0 (= 8 mod 4))
    = 4 (do until smaller one being 0, so then the other becomes GCD)

    >>> gcd_optimal_euclidean(1, 10)
    1
    >>> gcd_optimal_euclidean(45, 81)
    9
    >>> gcd_optimal_euclidean(1111, 10000000000001)
    11
    >>> gcd_optimal_euclidean(-20, 30)
    10
    """
    if b == 0:
        return a
    a, b = b, a % b
    return gcd_optimal_euclidean(a, b)
