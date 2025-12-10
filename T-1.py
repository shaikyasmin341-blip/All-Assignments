#Write python code for linear_search () function to search a value in a list and extract its index.

def linear_search(arr, target):
    for index in range(len(arr)):
        if arr[index] == target:
            return index
    return -1  # Return -1 if the target is not found
# Example usage:
my_list = [10, 20, 30, 40, 50]
target_value = 30
result = linear_search(my_list, target_value)
if result != -1:
    print(f"Element found at index: {result}")
else:
    print("Element not found in the list.")

    