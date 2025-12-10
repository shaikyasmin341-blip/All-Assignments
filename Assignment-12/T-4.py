# Task Description #4 – Gradient Descent Optimization
# Task: Find x that minimizes f(x) = 2x^3 + 4x + 5
def f(x):
    return 2 * x**3 + 4 * x + 5
def df(x):
    return 6 * x**2 + 4   # derivative of f(x)
def gradient_descent(starting_x, learning_rate, num_iterations):
    x = starting_x
    for i in range(num_iterations):
        grad = df(x)
        # Safety check to avoid overflow
        if abs(grad) > 1e6:
            print("Gradient exploded. Stopping early.")
            break
        x = x - learning_rate * grad
        # Value control to avoid very large numbers
        if abs(x) > 1e6:
            print("Value became too large. Stopping early.")
            break
    return x
# Parameters
starting_x = 0.0
learning_rate = 0.0001   # Smaller learning rate (prevents overflow)
num_iterations = 10000
# Run gradient descent
optimal_x = gradient_descent(starting_x, learning_rate, num_iterations)
print("Approximate x value returned by Gradient Descent:", optimal_x)
print("Value of f(x) at this point:", f(optimal_x))
