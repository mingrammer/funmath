def gcd_optimal_euclidean(a: int, b: int) -> int:
    if b == 0:
        return a
    a, b = b, a % b
    return gcd_optimal_euclidean(a, b)


def lcm_optimal_euclidean(a: int, b: int) -> int:
    """Return a LCM (Lowest Common Multiple) of given two integers using euclidean algorithm

    This function uses euclidean algorithm to get LCM of two integers.
    The LCM can be obtained by (a * b) / gcd(a, b), so we can use euclidean algorithm to get LCM by (a * b) / GCD.
    This algorithm works as follows.

    gcd(100, 36)
    = gcd(36, 28 (= 100 mod 36))
    = gcd(28, 8 (= 36 mod 28))
    = gcd(8, 4 (= 28 mod 8))
    = gcd(4, 0 (= 8 mod 4))
    = 4 (do until smaller one being 0, so then the other becomes GCD)

    So, the LCM will be (100 * 36) / 4 equals 900.

    >>> lcm_optimal_euclidean(3, 10)
    30
    >>> lcm_optimal_euclidean(42, 63)
    126
    >>> lcm_optimal_euclidean(4041, 8012)
    32376492
    >>> lcm_optimal_euclidean(-20, 30)
    60
    """
    gcd = gcd_optimal_euclidean(a, b)
    return abs(int((a * b) / gcd))
