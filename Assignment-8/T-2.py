#Task Description#2 (Loops)
#Ask AI to generate test cases for assign_grade(score) function. Handle boundary and invalid inputs.
#Requirements
# AI should generate test cases for assign_grade(score) where: 90-100: A, 80-89: B, 70-79: C, 60-69: D, <60: F
# Include boundary values and invalid inputs (e.g., -5, 105, "eighty").
#Expected Output#2
#Grade assignment function passing test suite

def assign_grade(score):
    if not isinstance(score, (int, float)):
        return "Invalid input"
    if score < 0 or score > 100:
        return "Invalid input"
    if 90 <= score <= 100:
        return 'A'
    elif 80 <= score < 90:
        return 'B'
    elif 70 <= score < 80:
        return 'C'
    elif 60 <= score < 70:
        return 'D'
    else:
        return 'F'
# Test cases for assign_grade function
def test_assign_grade():
    test_cases = [
        (95, 'A'),
        (89, 'B'),
        (75, 'C'),
        (65, 'D'),
        (50, 'F'),
        (90, 'A'),  # Boundary case
        (80, 'B'),  # Boundary case
        (70, 'C'),  # Boundary case
        (60, 'D'),  # Boundary case
        (0, 'F'),   # Boundary case
        (100, 'A'), # Boundary case
        (-5, 'Invalid input'),  # Invalid input
        (105, 'Invalid input'), # Invalid input
        ("eighty", 'Invalid input'), # Invalid input
    ]
    
    for score, expected in test_cases:
        result = assign_grade(score)
        assert result == expected, f"Test failed for score {score}: expected {expected}, got {result}"
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_assign_grade()