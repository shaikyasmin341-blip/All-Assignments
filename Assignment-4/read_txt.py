#“Write a Python function that reads a text file and returns the number of lines.
#Example 1: For a file with 3 lines → Output: 3
#Example 2: For a file with 0 lines → Output: 0
#Example 3: For a file with 5 lines → Output: 5”

def count_lines_in_file(file_path):
        # Open the file in read mode
        with open(file_path, 'r') as file:
            lines = file.readlines()
            return len(lines)


with open('example.txt', 'w') as f:
    f.write("Hello World\n")
    f.write("Welcome to AI Lab\n")
    f.write("My name is Yas\n")

print(count_lines_in_file('example.txt'))

