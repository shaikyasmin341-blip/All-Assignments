#Use AI to generate test cases for is_valid_email(email) and then implement the validator function.  

#Requirements:

#•	Must contain @ and . characters.
#•	Must not start or end with special characters.
#•	Should not allow multiple @.


#Expected Output#1
#•	Email validation logic passing all test cases 


import re
# Function to validate email addresses
def is_valid_email(email: str) -> bool:
    # Regular expression for validating an Email
    email_regex = r'^[a-zA-Z0-9]+[a-zA-Z0-9._%+-]*@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    # Check if email matches the regex
    if re.match(email_regex, email):
        # Check for multiple @ characters
        if email.count('@') == 1:
            return True
    return False

# Example usage
if __name__ == "__main__":
    test_emails = [
        "test@example.com",
        "invalid-email",
        "another.test@domain.co"
    ]

    for email in test_emails:
        print(f"Is '{email}' a valid email? {is_valid_email(email)}")

