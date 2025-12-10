#Task Description #2 – Error Handling in Legacy Code
"""Task: Legacy function without proper error handling
Python Code
def read_file(filename):
f = open(filename, "r")
data = f.read()
f.close()
return data
Expected Output:
AI refactors with with open() and try-except"""

def read_file(filename):
    try:
        with open(filename, "r") as f:
            data = f.read()
        return data

    except FileNotFoundError:
        return "Error: The file was not found."

    except IOError:
        return "Error: An I/O error occurred while reading the file."

    
# Example usage
if __name__ == "__main__":
    filename = "C:\\Users\\uts\\OneDrive\\Desktop\\All Assignments\\Assignment-13\\example.txt"
    content = read_file(filename)
    print(content)