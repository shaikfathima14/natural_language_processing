import re

resume = """
Name: Shaik Fathima
Email: fathima123@gmail.com
Mobile: 9876543210
Skills: Python, SQL, Machine Learning, NLP
Experience: 3 years
"""

# Name
name = re.search(r"Name:\s*(.*)", resume)
print("Name:", name.group(1))

# Email
email = re.findall(r'[\w\.-]+@[\w\.-]+\.\w+', resume)
print("Email:", email)

# Mobile
mobile = re.findall(r'\b\d{10}\b', resume)
print("Mobile:", mobile)

# Skills
skills = ["Python", "Java", "SQL", "Machine Learning", "NLP"]
found = []

for skill in skills:
    if re.search(skill, resume, re.IGNORECASE):
        found.append(skill)

print("Skills:", found)

# Experience
exp = re.search(r'(\d+)\s+years', resume)
years = int(exp.group(1))
print("Experience:", years, "years")

# Summary
print("\nCandidate Summary")
print("Name:", name.group(1))
print("Email:", email[0])
print("Mobile:", mobile[0])
print("Skills:", ", ".join(found))
print("Experience:", years, "years")

# Eligibility
if years >= 2 and "Python" in found:
    print("\nEligible for Shortlisting")
else:
    print("\nNot Eligible")