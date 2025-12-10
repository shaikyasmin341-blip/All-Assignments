#Task Description #1 – AI-generated HTML Page
"""Task: Ask AI to generate a simple HTML homepage for a "Student Info Portal" with a header, navigation menu, and footer.
Expected Output:
●	HTML code with <header>, <nav>, <footer>.
●	Clean indentation, proper tags, and comments."""

# AI-generated HTML code for a "Student Info Portal"
html_code = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Student Info Portal</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
        }
        header {
            background-color: #4CAF50;
            color: white;
            padding: 10px 0;
            text-align: center;
        }
        nav {
            background-color: #333;
        }
        nav a {
            color: white;
            padding: 14px 20px;
            text-decoration: none;
            display: inline-block;
        }
        nav a:hover {
            background-color: #ddd;
            color: black;
        }
        footer {
            background-color: #f1f1f1;
            text-align: center;
            padding: 10px 0;
            position: fixed;
            width: 100%;
            bottom: 0;
        }
    </style>
</head>
<body>

    <!-- Header Section -->
    <header>
        <h1>Welcome to the Student Info Portal</h1>
    </header>

    <!-- Navigation Menu -->
    <nav>
        <a href="#home">Home</a>
        <a href="#about">About</a>
        <a href="#courses">Courses</a>
        <a href="#contact">Contact</a>
    </nav>

    <!-- Main Content Area -->
    <main>
        <h2>Home</h2>
        <p>This is the homepage of the Student Info Portal where students can find information about their courses, schedules, and more.</p>
    </main>

    <!-- Footer Section -->
    <footer>
        <p>&copy; 2024 Student Info Portal. All rights reserved.</p>
    </footer>

</body>
</html>
"""
# Print the generated HTML code
print(html_code)
# Save the HTML code to a file
with open("student_info_portal.html", "w") as file:
    file.write(html_code)

    