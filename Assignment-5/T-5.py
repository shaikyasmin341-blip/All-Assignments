
# Task Description#5 (Inclusiveness)
# Code Snippet

#def greet_user(name, gender):
  # if gender.lower() == "male":
    #  title = "Mr."

# else:
    #    title = "Mrs."
    # return f"Hello, {title} {name}! Welcome."

# Expected Output#5
# Regenerate code that includes gender-neutral also


# ------------------------------------------------------------
# ------------------------------
# ✅ UNBIASED VERSION
# ------------------------------

def greet_user(name, gender):
    """
    Greets a user with an inclusive and respectful title.
    Supports male, female, non-binary, and unknown genders.
    """
    gender = gender.lower()
    if gender == "male":
        title = "Mr."
    elif gender == "female":
        title = "Ms."
    elif gender in ["non-binary", "nb", "neutral"]:
        title = "Mx."     # Accepted gender-neutral title
    else:
        title = ""        # When gender not provided or unknown
    return f"Hello, {title} {name}! Welcome."

# Example usage
print(greet_user("Alex", "male"))
print(greet_user("Jordan", "female"))
print(greet_user("Taylor", "non-binary"))
print(greet_user("Sam", "unknown"))