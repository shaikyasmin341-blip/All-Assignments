#“Write a Python function that counts the number of vowels in a string.
#Example 1: ‘hello’ → 2
#Example 2: ‘PYTHON’ → 1
#Example 3: ‘Education’ → 5”

def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count
    
print(count_vowels("hello"))      
print(count_vowels("PYTHON"))
print(count_vowels("Education"))