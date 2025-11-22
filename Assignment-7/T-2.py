#Identify and fix a logic error in a loop that causes infinite iteration

# Original function with a logic error causing infinite loop
def count_up_to(n):
    count = 1
    while count <= n:
        print(count)
        # Logic error: count is not being incremented, causing infinite loop
        count += 1  # Fixed by adding this line to increment count
count_up_to(5)
# Fixed function with the logic error corrected
def count_up_to(n):
    count = 1
    while count <= n:
        print(count)
        count += 1  # Increment count to avoid infinite loop
count_up_to(5)