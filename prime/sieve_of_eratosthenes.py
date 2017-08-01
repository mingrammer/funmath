from typing import List


def sieve_of_eratosthenes(n: int) -> List[int]:
    """Return a list of prime numbers which are less than the given integer using sieve of eratosthenes method

    >>> sieve_of_eratosthenes(1)
    []
    >>> sieve_of_eratosthenes(10)
    [2, 3, 5, 7]
    >>> sieve_of_eratosthenes(50)
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    >>> sieve_of_eratosthenes(-37)
    Traceback (most recent call last):
        ...
    ValueError: n must be >= 1
    """
    if n < 1:
        raise ValueError("n must be >= 1")
    sieve = [True] * n
    sieve[0] = False
    for i in range(2, n + 1):
        if sieve[i - 1]:
            for j in range(i ** 2, n + 1, i):
                sieve[j - 1] = False
    prime_list = []
    for i, is_prime in enumerate(sieve):
        if is_prime:
            prime_list.append(i + 1)
    return prime_list
