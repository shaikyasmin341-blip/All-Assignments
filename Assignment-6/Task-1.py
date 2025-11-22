#Write a Python class named Student with attributes like name, roll_number, and marks. Include a method display_details() that prints all details of the student.

class Student:
    def __init__(self, name, roll_number, marks):
        self.name = name
        self.roll_number = roll_number
        self.marks = marks

    def display_details(self):
        print("Name:", self.name)
        print("Roll Number:", self.roll_number)
        print("Marks:", self.marks)
# Example usage:
student1 = Student("Alice", 101, 95)
student1.display_details()

student2 = Student("Bob", 102, 88)
student2.display_details()
