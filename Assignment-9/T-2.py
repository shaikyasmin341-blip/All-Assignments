#	Task Description#2 Automatic Inline Comments
#	Write python program for sru_student class with attributes like name, roll no., hostel_status and fee_update method and display_details method.
#	Write comments manually for each line/code block
#	Ask an AI tool to add inline comments explaining each line/step.
#	Compare the AI-generated comments with your manually written one.

# Expected Output#2: Students critically analyze AI-generated code comments. 


class sru_student:
    def __init__(self, name, roll_no, hostel_status):
        # Manually written comment: Initialize the sru_student object with name, roll number, and hostel status
        self.name = name  # Student's name
        self.roll_no = roll_no  # Student's roll number
        self.hostel_status = hostel_status  # Hostel status (True/False)

    def fee_update(self, amount):
        # Manually written comment: Update the fee status of the student
        # AI-generated comment: This method updates the fee status of the student by a given amount.
        print(f"Fee updated by {amount} for student {self.name}")

    def display_details(self):
        # Manually written comment: Display the details of the student
        # AI-generated comment: This method displays the student's details including name, roll number, and hostel status.
        print(f"Name: {self.name}, Roll No: {self.roll_no}, Hostel Status: {self.hostel_status}")
# AI-generated docstring:
    """
    This class represents a student at SRU with attributes for name, roll number, and hostel status.
    
    Methods:
        fee_update(amount): Updates the fee status of the student by a given amount.
        display_details(): Displays the student's details including name, roll number, and hostel status.
    """
    def __init__(self, name, roll_no, hostel_status):
        self.name = name
        self.roll_no = roll_no
        self.hostel_status = hostel_status

    def fee_update(self, amount):
        print(f"Fee updated by {amount} for student {self.name}")

    def display_details(self):
        print(f"Name: {self.name}, Roll No: {self.roll_no}, Hostel Status: {self.hostel_status}")