#Debug a runtime error caused by division by zero. Let AI insert try-except.

# Original function that may cause division by zero error
def divide(a, b):
    return a / b
# Fixed function with try-except to handle division by zero
def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
    return result

# Example usage
print(divide(10, 2))  # Should print 5.0
print(divide(10, 0))  # Should print error message
