# Task Description#1 Basic Docstring Generation
# •	Write python function to return sum of even and odd numbers in the given list.  
# •	Incorporate manual docstring in code with Google Style
# •	Use an AI-assisted tool (e.g., Copilot,  Cursor AI) to generate a docstring describing the function.
# •	Compare the AI-generated docstring with your manually written one.
# Expected Outcome#1: Students understand how AI can produce function-level documentation


def sum_even_odd(numbers):
    """
    Calculate the sum of even and odd numbers in a given list.

    This function takes a list of integers as input and returns a tuple containing
    the sum of even numbers and the sum of odd numbers.

    Args:
        numbers (list): A list of integers.

    Returns:
        tuple: A tuple containing two integers:
            - The sum of even numbers in the list.
            - The sum of odd numbers in the list.

    """
    even_sum = sum(num for num in numbers if num % 2 == 0)
    odd_sum = sum(num for num in numbers if num % 2 != 0)
    return even_sum, odd_sum
# AI-generated docstring:
    """
    This function takes a list of integers and returns the sum of even and odd numbers.

    Args:
        numbers (list): A list of integers.
    Returns:
        tuple: A tuple containing the sum of even numbers and the sum of odd numbers.
    """
    even_sum = sum(num for num in numbers if num % 2 == 0)
    odd_sum = sum(num for num in numbers if num % 2 != 0)
    return even_sum, odd_sum
    """

    This function takes a list of integers and returns the sum of even and odd numbers.
    Args:
        numbers (list): A list of integers.
    Returns:
        tuple: A tuple containing the sum of even numbers and the sum of odd numbers.
    """
    even_sum = sum(num for num in numbers if num % 2 == 0)
    odd_sum = sum(num for num in numbers if num % 2 != 0)
    return even_sum, odd_sum
    even_sum = sum(num for num in numbers if num % 2 == 0)
    odd_sum = sum(num for num in numbers if num % 2 != 0)
    return even_sum, odd_sum
    even_sum = sum(num for num in numbers if num % 2 == 0)
    odd_sum = sum(num for num in numbers if num % 2 != 0)
    return even_sum, odd_sum