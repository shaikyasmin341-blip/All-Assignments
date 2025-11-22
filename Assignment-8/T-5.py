# Task Description#5
# Use AI to write test cases for convert_date_format(date_str) to switch from "YYYY-
# MM-DD" to "DD-MM-YYYY".
# Example: "2023-10-15" → "15-10-2023"
# Function converts input format correctly for all test cases

def convert_date_format(date_str):
    try:
        year, month, day = date_str.split('-')

        # Check correct length
        if len(year) != 4 or len(month) != 2 or len(day) != 2:
            return "Invalid date format"

        # Check numeric
        if not (year.isdigit() and month.isdigit() and day.isdigit()):
            return "Invalid date format"

        # Convert to integers
        y, m, d = int(year), int(month), int(day)

        # Validate ranges
        if m < 1 or m > 12:
            return "Invalid date format"
        if d < 1 or d > 31:
            return "Invalid date format"

        return f"{day}-{month}-{year}"

    except ValueError:
        return "Invalid date format"


# Test cases for convert_date_format function
def test_convert_date_format():
    test_cases = [
        ("2023-10-15", "15-10-2023"),
        ("1999-01-01", "01-01-1999"),
        ("2000-12-31", "31-12-2000"),
        ("2024-02-29", "29-02-2024"),  # Leap year
        ("2021-04-30", "30-04-2021"),

        ("abcd-ef-gh", "Invalid date format"),  # Invalid format
        ("2023/10/15", "Invalid date format"),  # Wrong separator
        ("20231015", "Invalid date format"),    # No separators

        # These should now return INVALID (as expected)
        ("2023-13-01", "Invalid date format"),  
        ("2023-00-10", "Invalid date format"),  
        ("2023-10-32", "Invalid date format"),  
    ]

    for date_str, expected in test_cases:
        result = convert_date_format(date_str)
        assert result == expected, f"Test failed for date '{date_str}': expected {expected}, got {result}"

    print("All test cases passed!")

if __name__ == "__main__":
    test_convert_date_format()
