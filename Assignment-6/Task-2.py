#Prompt AI to complete a function that prints the first 10 multiples of a number using a loop.

def print_multiples(number):
    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")


print_multiples(5)

