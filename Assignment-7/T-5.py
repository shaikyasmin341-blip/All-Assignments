#Access an invalid list index and use AI to resolve the Index Error.

my_list = [10, 20, 30, 40, 50]
try:
    # Attempting to access an index that is out of range
    print(my_list[10])
except IndexError as e:
    print("IndexError encountered:", e)
    print("The index you are trying to access is out of range.")
    print("The valid indices for this list are from 0 to", len(my_list) - 1)
    print("Please use a valid index within this range.")

# Correcting the index to a valid one
valid_index = 2
print("Accessing a valid index:", my_list[valid_index])
