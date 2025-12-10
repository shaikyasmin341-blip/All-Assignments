"""Task Description #3 – Complex Refactoring
Task: Provide this legacy class to AI for readability and modularity improvements:

Python Code"""

class Student:
    def __init__(self, n, a, m1, m2, m3):
        self.n = n
        self.a = a
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
    def details(self):
        print("Name:", self.n, "Age:", self.a)
    def total(self):
        return self.m1+self.m2+self.m3
"""Expected Output:
•	AI improves naming (name, age, marks).
•	Adds docstrings.
•	Improves print readability.
•	Possibly uses sum(self.marks) if marks stored in a list"""

class Student:
    def __init__(self, name, age, marks):
        """
        Initialize a Student object with name, age, and marks.

        :param name: str - The name of the student.
        :param age: int - The age of the student.
        :param marks: list - A list of marks obtained by the student.
        """
        self.name = name
        self.age = age
        self.marks = marks

    def display_details(self):
        """Print the student's details in a readable format."""
        print(f"Student Name: {self.name}, Age: {self.age}")

    def calculate_total_marks(self):
        """
        Calculate the total marks obtained by the student.

        :return: int - The total marks.
        """
        return sum(self.marks)
    
# Example usage
if __name__ == "__main__":
    student = Student("Alice", 20, [85, 90, 95])
    student.display_details()
    total_marks = student.calculate_total_marks()
    print(f"Total Marks: {total_marks}")