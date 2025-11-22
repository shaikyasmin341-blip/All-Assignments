# Function to calculate factorial using recursion
def factorial(n: int) -> int:
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)    
# Function to calculate factorial using iteration
def factorial_iterative(n: int) -> int:
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

#  Example usage
print(factorial(5))           # Output: 120
print(factorial_iterative(5))  # Output: 120
print(factorial(2))           # Output: 2
print(factorial_iterative(2))  # Output: 2