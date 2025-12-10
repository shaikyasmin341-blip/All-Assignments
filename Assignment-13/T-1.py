"""Task Description #1 – Remove Repetition
Task: Provide AI with the following redundant code and ask it to refactor
Python Code
def calculate_area(shape, x, y=0):
    if shape == "rectangle":
        return x * y
    elif shape == "square":
        return x * x
    elif shape == "circle":
        return 3.14 * x * x

Expected Output
•	Refactored version with dictionary-based dispatch or separate functions.
•	Cleaner and modular design."""
def calculate_area(shape, x, y=0):
    def area_rectangle(x, y):
        return x * y
    def area_square(x):
        return x * x
    def area_circle(x):
        return 3.14 * x * x
    shape_functions = {
        "rectangle": area_rectangle,
        "square": area_square,
        "circle": area_circle
    }
    if shape in shape_functions:
        if shape == "rectangle":
            return shape_functions[shape](x, y)
        else:
            return shape_functions[shape](x)
    else:
        raise ValueError("Unknown shape")