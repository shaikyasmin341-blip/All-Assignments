# Function to find the largest number in a list

def largest_number(numbers: list) -> int:
    if not numbers:
        raise ValueError("The list is empty.")
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num

# Example usage
print(largest_number([3, 5, 2, 8, 1]))  # Output: 8
print(largest_number([-10, -5, -2, -8, -1]))  # Output: -1
print(largest_number([0, 0, 0, 0]))  # Output: 0
print(largest_number([100, 200, 50, 300, 150]))  # Output: 300