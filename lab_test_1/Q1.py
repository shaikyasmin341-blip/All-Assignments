# Create a function to reverse a list in Python. Use an AI tool to suggest alternative implementations. Test and compare the performance of each version.
#prompt:
""" You are an expert Python programmer. Create a function to reverse a list in Python. Provide at least three different implementations using different approaches (e.g., slicing, built-in functions, loops). Test and compare the performance of each version using the time module. Here is a Python implementation with multiple versions of the reverse function and performance testing:"""
import time
def reverse_list_v1(lst):
    """Reverse a list using slicing."""
    return lst[::-1]
def reverse_list_v2(lst):
    """Reverse a list using the reversed() function."""
    return list(reversed(lst))
def reverse_list_v3(lst):
    """Reverse a list using a for loop."""
    reversed_lst = []
    for item in lst:
        reversed_lst.insert(0, item)
    return reversed_lst

def test_performance(func, lst, iterations=10000):
    start_time = time.time()
    for _ in range(iterations):
        func(lst)
    end_time = time.time()
    return end_time - start_time
if __name__ == "__main__":
    test_list = list(range(1000))  # A sample list to reverse
    iterations = 1000  # Number of iterations for performance testing

    time_v1 = test_performance(reverse_list_v1, test_list, iterations)
    time_v2 = test_performance(reverse_list_v2, test_list, iterations)
    time_v3 = test_performance(reverse_list_v3, test_list, iterations)

    print(f"Performance of reverse_list_v1 (slicing): {time_v1:.6f} seconds")
    print(f"Performance of reverse_list_v2 (reversed function): {time_v2:.6f} seconds")
    print(f"Performance of reverse_list_v3 (for loop): {time_v3:.6f} seconds")

    # Determine the fastest implementation
    times = {
        "reverse_list_v1": time_v1,
        "reverse_list_v2": time_v2,
        "reverse_list_v3": time_v3
    }

    fastest = min(times, key=times.get)
    print(f"The fastest implementation is {fastest} with a time of {times[fastest]:.6f} seconds")