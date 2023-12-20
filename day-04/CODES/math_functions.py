# MATH FUNCTIONS

# Import the 'math' module, which provides mathematical functions and constants in Python.
import math

# Fields for examples of math functions.
num_one = 10
num_two = 5
angle_rad = math.radians(30)


# Basic Arithmetic Operations - Python's built-in math functions facilitate fundamental arithmetic operations.

sum_result = num_one + num_two  # Addition
difference_result = num_one - num_two  # Subtraction
product_result = num_one * num_two  # Multiplication
quotient_result = num_one / num_two  # Division


# Power and Square Root - The `math.pow()` calculates the power of a number, while `math.sqrt()` efficiently computes its square root.

power_result = math.pow(num_one, 2)  # Power of 10^2
sqrt_result = math.sqrt(num_one)


# Rounding Functions - The `round()` function in Python rounds a floating-point number to the nearest integer, while `math.trunc()` truncates a floating-point number to an integer.

rounded_result = round(8.5)
truncated_result = math.trunc(8.9)


# Ceiling and Floor Functions - The `math.ceil()` rounds up to the nearest integer, and `math.floor()` rounds down, providing precise control over numeric values.

ceil_result = math.ceil(8.3)
floor_result = math.floor(8.7)


# Absolute Value - The `math.fabs()` calculates the absolute value of a given number, providing the positive magnitude regardless of its sign.

absolute_result = math.fabs(-10)


# Constants - Python's `math` module includes constants like `math.pi` for pi and `math.e` for Euler's number, providing accurate values for mathematical computations.

pi_value = math.pi
e_value = math.e


# Trigonometric Functions - Python's `math` module provides trigonometric functions like `math.sin()`, `math.cos()`, and `math.tan()`.

sin_result = math.sin(angle_rad)
cos_result = math.cos(angle_rad)
tan_result = math.tan(angle_rad)


# Exponential and Logarithmic Functions - Python's `math` module has `math.exp()` for exponentiation and `math.log()` and `math.log10()` for logarithmic computations.

exp_result = math.exp(num_one)
log_result = math.log(num_one, 10)  # Logarithm to the base 10
