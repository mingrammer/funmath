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
* differential
  * polynomials
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
* pytagorean_numbers
* square_root
* trigonometric_functions

<br>

## Contribute

* You can implement any sort of algorithms for mathematical things.
  * If you add new kind of algorithms, please also add that in README as new category.
  * If you want to add other programming language version of existing solutions, you must name the source code file as same to existing one.
  * It is better to provide the explains of your algorithms in comments of source code files.
* You can use any programming languages you are preferring, but you **SHOULD** take care of handling large numbers. And if you want to contribute the algorithms with Python, you **SHOULD** write the scripts with Python 3.6+.
* You must have to write the test codes for each algorithms. See the [example](fibonacci/fibonacci_optimal_memoization.py) for writing the tests (the example is written in Python)
* It is not recommended to use the builtin math libraries as possible. Because this repository encourages that implement the mathematical things by ourselves.
* It is better to provide the optimal solutions as well for each algorithms.

<br>

## Contributors
- [@mingrammer](https://github.com/mingrammer)
