def next_prime(number:int):
    """Find the next prime after the input
    >>> next_prime(3)
    5
    >>> next_prime(1421)
    1423
    >>> next_prime(-26)
    ValueError: Number must be >= 1
    >>> next_prime(80023045)
    80023051
    """
    if number <= 0 :   raise ValueError("Number must be >= 1")
    number = number + 1
    for p in range(number, 2*number):
        for i in range(2, p):
            if p % i == 0:
                break
        else:
            return p
