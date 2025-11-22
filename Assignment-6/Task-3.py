# Ask AI to write nested if-elif-else conditionals to classify age groups using conditional statements.

age = int(input("Enter your age: "))
if age < 0:
    print("Invalid age")
elif age <= 12:
    print("Child")
elif age <= 19:
    print("Teenager")
elif age <= 64:
    print("Adult")
else:
    print("Senior")


