import re

register = input("Enter Register Number: ")
email = input("Enter College Email: ")
course = input("Enter Course Code: ")
semester = input("Enter Semester: ")
mobile = input("Enter Mobile Number: ")

valid = True

# Register Number
if re.fullmatch(r'\d{12}', register):
    print("Register Number: Valid")
else:
    print("Register Number: Invalid")
    valid = False

# Email
if re.fullmatch(r'[\w\.-]+@saveetha\.com', email):
    print("Email: Valid")
else:
    print("Email: Invalid")
    valid = False

# Course Code
if re.fullmatch(r'[A-Z]{2,4}\d{3}', course):
    print("Course Code: Valid")
else:
    print("Course Code: Invalid")
    valid = False

# Semester
if re.fullmatch(r'[1-8]', semester):
    print("Semester: Valid")
else:
    print("Semester: Invalid")
    valid = False

# Mobile Number
if re.fullmatch(r'[6-9]\d{9}', mobile):
    print("Mobile Number: Valid")
else:
    print("Mobile Number: Invalid")
    valid = False

# Final Status
if valid:
    print("\nRegistration Successful")
else:
    print("\nRegistration Failed")