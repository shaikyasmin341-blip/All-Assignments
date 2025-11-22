#Task Description#3
#Generate test cases using AI for is_sentence_palindrome(sentence). Ignore case,punctuation, and spaces
#Requirement
#Ask AI to create test cases for is_sentence_palindrome(sentence)(ignores case, spaces, and punctuation).
#Example:
#"A man a plan a canal Panama" → True
#Expected Output#3
#Function returns True/False for cleaned sentences
#Implement the function to pass AI-generated tests
import string
def is_sentence_palindrome(sentence):
    # Clean the sentence: remove punctuation, convert to lowercase, and remove spaces
    cleaned = ''.join(char.lower() for char in sentence if char.isalnum())
    return cleaned == cleaned[::-1]
# Test cases for is_sentence_palindrome function
def test_is_sentence_palindrome():
    test_cases = [ 
        ("A man a plan a canal Panama", True),
        ("No 'x' in Nixon", True),
        ("Was it a car or a cat I saw?", True),
        ("Hello World", False),
        ("", True),  # Empty string
        (" ", True),  # String with only spaces
        ("Able was I ere I saw Elba", True),
        ("This is not a palindrome", False),
        ("12321", True),  # Numeric palindrome
        ("12345", False), # Non-palindrome numeric
    ]
    for sentence, expected in test_cases:
        result = is_sentence_palindrome(sentence)
        assert result == expected, f"Test failed for sentence '{sentence}': expected {expected}, got {result}"
    print("All test cases passed!")
if __name__ == "__main__":
    test_is_sentence_palindrome()

