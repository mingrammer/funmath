<br><br>

<h1 align="center">FUN MATH</h1>

<p align="center">
  <a href="/LICENSE"><img src="https://img.shields.io/badge/license-MIT-blue.svg"/></a>
  <a href="https://app.fossa.io/projects/git%2Bgithub.com%2Fmingrammer%2Ffunmath?ref=badge_shield" alt="FOSSA Status"><img src="https://app.fossa.io/api/projects/git%2Bgithub.com%2Fmingrammer%2Ffunmath.svg?type=shield"/></a>
  <a href="https://docs.python.org/3/index.html"><img src="https://img.shields.io/badge/python-3.6-blue.svg"/></a>
</p>

<p align="center">
  Implementations of mathematical functions, formulas and concepts
</p>

<br><br><br>

It provides the mathematical implementations for various topics which are related to mathematical things such as fibonacci, euclidean, prime numbers and so on. Any mathematical topics or concepts are welcome. If you love the math, join to here with your algorithms and codes!

This repository does not force for using the specific programming languages, but if you are using the Python, you should use the Python 3.6 to contribute or to run. (you wiil use the only Python 3.6+ in the future)

A solution can be implemented in three ways:

- **By definition** solution, a mathematical definition. Good example is the fibonacci series. But the solution by definition of the fibonacci has worst performance
- **Optimal** solution which has better performance than by definition one (or best solution).
- **Creative** solution. This may not be optimal one, but creative or funny way.

## Run

* Python
  * `python3 -m doctest <path>/<script_name.py> -v`

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
  * [factorial_recursion.py](factorial/factorial_recursion.py)
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
  * [is_prime_improved.py](prime/is_prime_improved.py)
  * [is_prime_optimal.py](prime/is_prime_optimal.py)
  * [next_prime.py](prime/next_prime.py)
  * [sieve_of_eratosthenes.py](prime/sieve_of_eratosthenes.py)
* [pythagorean_triple](pythagorean_triple)
  * [pythagorean_triple.py](pythagorean_triple/pythagorean_triple.py)
* square_root
* [trigonometric_functions](trigonometric_functions)
  * [trig.py](trigonometric_functions/trig.py)

## Contribution

* You can implement any sort of algorithms for mathematical things.
  * If you add new kind of algorithms, please also add that in README as new category.
  * If you want to add other programming language version of existing solutions, you must name the source code file as same to existing one.
  * It is better to provide the explains of your algorithms in comments of source code files.
* You can use any programming languages you are preferring, but you **SHOULD** take care of handling large numbers. And if you want to contribute the algorithms with Python, you **SHOULD** write the scripts with Python 3.6+.
* You **MUST** have to write the test codes for each algorithms. See the [example](fibonacci/fibonacci_optimal_memoization.py) for writing the tests (the example is written in Python)
* It is not recommended to use the builtin math libraries as possible. Because this repository encourages that implement the mathematical things by ourselves.
* It is better to provide the optimal solutions as well for each algorithms.

## Changelog
> **Enhancement**
> - Link the Travis CI to run the tests when commits [#4](../../issues/4)
>
> **Fixed**
> - Don't check the weird invalid type on functions which accept only specific types [#3](../../issues/3)
> - Remove the stricted type checking on some functions [#2](../../issues/2)

## Contributors

- [@mingrammer](https://github.com/mingrammer)
- [@Xaltonon](https://github.com/Xaltonon )
- [@TsimpDim](https://github.com/TsimpDim)

## License

[![FOSSA Status](https://app.fossa.io/api/projects/git%2Bgithub.com%2Fmingrammer%2Ffunmath.svg?type=large)](https://app.fossa.io/projects/git%2Bgithub.com%2Fmingrammer%2Ffunmath?ref=badge_large)
