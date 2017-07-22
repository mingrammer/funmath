![python](https://img.shields.io/badge/python-3.6-blue.svg) ![travis](https://travis-ci.org/mingrammer/funmath.svg?branch=master)

# funmath
Implementations of mathematical functions, formulas and concepts.

It provides the implementations of various topics for mathematical things such as fibonacci, euclidean, prime numbers and so on. Any mathematical topics or concepts are welcome. If you love the math, join to here with your algorithms and codes!

This repository does not force the specific programming languages, but if you are using the Python, you should use the Python 3.6 to contribute or to run. (you wiil use the only Python 3.6+ in the future)

There can be three types of implementations.

- **By definition** solutions (a mathematical definition. Good examples is fibonacci function. But the solution by definition of the fibonacci has worst performance)
- **Optimal** solutions which have better performance than by definition one.
- **Creative** solutions. This may not be optimal one, but creative or funny solutions.

<br>

## Run

* Python
  * `python3 -m doctest <path>/<script_name.py> -v`

<br>

## Implementations

* [abs](abs)
  * [abs.py](abs/abs.py)
* combinations
* decomposition
* [differentiation](differentiation)
  * [simple_numerical_differentiation.py](differentiation/simple_numerical_differentiation.py)
* [euclidean](euclidean)
  * [distance.py](euclidean/distance.py)
* [factorial](factorial)
  * [factorial.py](factorial/factorial.py)
* [fibonacci](fibonacci)
  * [fibonacci.py](fibonacci/fibonacci.py)
  * [fibonacci_optimal_memoization.py](fibonacci/fibonacci_optimal_memoization.py)
  * [fibonacci_optimal_iteration.py](fibonacci/fibonacci_optimal_iteration.py)
* [gcd](gcd)
  * [gcd.py](gcd/gcd.py)
  * [gcd_optimal_euclidean.py](gcd/gcd_optimal_euclidean.py)
* integral
* [lcm](lcm)
  * [lcm.py](lcm/lcm.py)
  * [lcm_optimal_euclidean.py](lcm/lcm_optimal_euclidean.py)
* matrix
  * multiplication
  * multiplication_optimal
* permutations
* [prime](prime)
  * [is_prime.py](prime/is_prime.py)
  * [is_prime_optimal.py](prime/is_prime_optimal.py)
* [pythagorean_triple](pythagorean_triple)
  * [pythagorean_triple.py](pythagorean_triple/pythagorean_triple.py)
* square_root
* trigonometric_functions
  * [trig.py](trigonometric_functions/trig.py)

<br>

## Contribution

* You can implement any sort of algorithms for mathematical things.
  * If you add new kind of algorithms, please also add that in README as new category.
  * If you want to add other programming language version of existing solutions, you must name the source code file as same to existing one.
  * It is better to provide the explains of your algorithms in comments of source code files.
* You can use any programming languages you are preferring, but you **SHOULD** take care of handling large numbers. And if you want to contribute the algorithms with Python, you **SHOULD** write the scripts with Python 3.6+.
* You **MUST** have to write the test codes for each algorithms. See the [example](fibonacci/fibonacci_optimal_memoization.py) for writing the tests (the example is written in Python)
* It is not recommended to use the builtin math libraries as possible. Because this repository encourages that implement the mathematical things by ourselves.
* It is better to provide the optimal solutions as well for each algorithms.

<br>

## Changelog
> **Enhancement**
> - Link the Travis CI to run the tests when commits [#4](../../issues/4)
>
> **Fixed**
> - Don't check the weird invalid type on functions which accept only specific types [#3](../../issues/3)
> - Remove the stricted type checking on some functions [#2](../../issues/2)

<br>

## Contributors

- [@mingrammer](https://github.com/mingrammer)
- [@Xaltonon](https://github.com/Xaltonon )
