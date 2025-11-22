#Write a Python function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            print(f"{n} is not a prime number.")
            return False
    print(f"{n} is a prime number.")
    return True

# Example usage

print(is_prime(2))  # True
print(is_prime(11))  # True
print(is_prime(4))   # False
print(is_prime(15))  # False
