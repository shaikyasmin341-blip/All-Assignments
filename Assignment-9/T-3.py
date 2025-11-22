# Task Description#3 
#	Write a Python script with 3–4 functions (e.g., calculator: add, subtract, multiply, divide).
#	Incorporate manual docstring in code with NumPy Style
#	Use AI assistance to generate a module-level docstring + individual function docstrings.
#	Compare the AI-generated docstring with your manually written one.

# Expected Output#3: Students learn structured documentation for multi-function scripts

def add(a, b):
    """Add two numbers.
    Parameters
    ----------
    a : float
        The first number.
    b : float
        The second number.
    Returns
    -------
    float
        The sum of a and b.
    """
    return a + b
def subtract(a, b):
    """Subtract two numbers.
    Parameters
    ----------
    a : float
        The first number.
    b : float
        The second number.
    Returns
    -------
    float
        The difference of a and b.
    """
    return a - b
def multiply(a, b):
    """Multiply two numbers.
    Parameters
    ----------
    a : float
        The first number.
    b : float
        The second number.
    Returns
    -------
    float
        The product of a and b.
    """
    return a * b
def divide(a, b):
    """Divide two numbers.
    Parameters
    ----------
    a : float
        The numerator.
    b : float
        The denominator.
    Returns
    -------
    float
        The quotient of a and b.
    Raises
    ------
    ValueError
        If b is zero.
    """
    if b == 0:
        raise ValueError("Denominator cannot be zero.")
    return a / b

    