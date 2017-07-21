import math

MACLAURIN_SERIES_TERMS = 20

def sin(x):
    """Returns the sine of x (in radians)

    This uses the Maclaurin expansion of sine to compute sines for the
    first quadrant of the unit circle.  Anything outsides of the range
    [0,π/2] is calculated by exploiting the symmetry of sine.

    >>> abs(sin(0)) < 1e-6
    True
    >>> abs(sin(math.pi/2) - 1) < 1e-6
    True
    >>> abs(sin(math.pi*3/2) - (-1)) < 1e-6
    True
    >>> abs(sin(math.pi*100)) < 1e-6
    True
    >>> abs(sin(math.pi/4) - 1/2**0.5) < 1e-6
    True
    >>> abs(sin(math.pi/3) - sin(math.pi/3*2)) < 1e-6
    True
    """
    def sin_quadrant(x):
        s = 0
        sign = 1
        for i in range(1, MACLAURIN_SERIES_TERMS, 2): 
            s += (x**i) / math.factorial(i) * sign
            sign *= -1
        return s
    quad = quadrant(x)
    norm = x % (math.pi/2)
    if quad == 1:
        return sin_quadrant(norm)
    elif quad == 2:
        return sin_quadrant(math.pi/2-norm)
    elif quad == 3:
        return -sin_quadrant(norm)
    elif quad == 4:
        return -sin_quadrant(math.pi/2-norm)

def cos(x):
    """Returns the cosine of x (in radians)

    This uses the identity cos(θ) = sin(θ+π/2)

    >>> abs(cos(0) - 1) < 1e-6
    True
    >>> abs(cos(math.pi) - (-1)) < 1e-6
    True
    >>> abs(cos(math.pi*3/2)) < 1e-6
    True
    >>> abs(cos(math.pi*100) - 1) < 1e-6
    True
    >>> abs(cos(math.pi/4) - sin(math.pi/4)) < 1e-6
    True
    """
    return sin(x+math.pi/2)

def tan(x):
    """Returns the tangent of x (in radians)

    This uses the identity tan(θ) = sin(θ)/cos(θ)

    >>> abs(tan(1) - sin(1)/cos(1)) < 1e-6
    True
    >>> abs(tan(math.pi*100)) < 1e-6
    True
    """
    return sin(x)/cos(x)

def quadrant(x):
    """Returns which quadrant of the unit circle x is in.
    """
    norm = x % (math.pi*2)
    quad = x % (math.pi/2)
    if 0 <= norm < math.pi/2:               # first quadrant
        return 1
    elif math.pi/2 <= norm < math.pi:       # second quadrant
        return 2
    elif math.pi <= norm < math.pi*(3/2):   # third quadrant
        return 3
    elif math.pi*(3/2) <= norm < math.pi*2: # fourth quadrant
        return 4
