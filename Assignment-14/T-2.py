"""Task Description #2 – CSS Styling
Task:
Use AI to add CSS styling to Task #1 homepage for:
●	Responsive navigation bar.
●	Centered content section.
●	Footer with light gray background.
Expected Output:
●	HTML + CSS combined.
●	AI explains how CSS classes apply.
Expected Output: AI refactors with with open() and try-except:"""

from pydoc import html
# Refactored AI-generated HTML code with CSS styling for "Student Info Portal"
    
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
            overflow: hidden;
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
        .content {
            text-align: center;
            margin: 20px;
        }
        footer {
            background-color: #f1f1f1;
            text-align: center;
            padding: 10px 0;
            position: fixed;
            width: 100%;
            bottom: 0;
        }
        @media screen and (max-width: 600px) {
            nav a {
                float: none;
                display: block;
                text-align: left;
            }
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
    <div class="content">
        <h2>Student Information</h2>
        <p>This portal provides access to student resources, course information, and contact details.</p>
    </div>

    <!-- Footer Section -->
    <footer>
        <p>&copy; 2024 Student Info Portal. All rights reserved.</p>
    </footer>

</body>
</html>
"""
try:
    with open("Student_Info_Portal.html", "w") as file:
        file.write(html_code)
    print("HTML file with CSS styling has been created successfully.")
except Exception as e:
    print(f"An error occurred while writing the file: {e}")
