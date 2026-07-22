import re

# Get input from the user
text = input("Enter a text: ")
pattern = input("Enter the pattern to search: ")

# Search for the pattern
matches = re.findall(pattern, text)

# Display the result
if matches:
    print("Pattern found:")
    print(matches)
else:
    print("Pattern not found.")