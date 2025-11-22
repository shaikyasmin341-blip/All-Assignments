# Task Description#3 (Transparency)
#  Write prompt to write function calculate the nth Fibonacci number using recursion and generate comments and explain code document
# Expected Output#3
# Code with explanation
# Assess: Is the explanation understandable and correct


def fibonacci(n):
    """
    Calculate the nth Fibonacci number using recursion.
    The Fibonacci sequence is defined as follows:
    - F(0) = 0
    - F(1) = 1
    - F(n) = F(n-1) + F(n-2) for n > 1

    This function takes an integer n and returns the nth Fibonacci number.
    """
    if n < 0:
        raise ValueError("Input should be a non-negative integer.")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
print(fibonacci(10))  # Output: 55
# Explanation:
# The function `fibonacci` calculates the nth Fibonacci number using a recursive approach.
# It first checks if the input n is a non-negative integer. If n is 0 or 1, it returns n directly.
# For values of n greater than 1, it recursively calls itself to compute the sum of the two preceding Fibonacci numbers.
# The explanation provided is clear and correct, detailing the function's purpose, input validation, base cases, and recursive logic.