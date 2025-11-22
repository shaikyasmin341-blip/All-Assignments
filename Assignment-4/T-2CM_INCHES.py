#Write a Python function to convert centimeters to inches.
#Example: 10 cm = 3.937 inches.

def cm_to_inches(cm):

    inches = cm / 2.54
    return inches

print(cm_to_inches(10))
print(cm_to_inches(25.4))