import re

products = [
    "Laptop",
    "Laptop Bag",
    "Wireless Mouse",
    "Gaming Laptop",
    "Keyboard",
    "Smartphone",
    "Phone Cover"
]

keyword = input("Enter search keyword: ")

print("\nExact Match")
exact = [p for p in products if re.fullmatch(keyword, p, re.I)]
print(exact)

print("\nPrefix Match")
prefix = [p for p in products if re.match(keyword, p, re.I)]
print(prefix)

print("\nSuffix Match")
suffix = [p for p in products if re.search(keyword + r'$', p, re.I)]
print(suffix)

print("\nPartial Match")
partial = [p for p in products if re.search(keyword, p, re.I)]
print(partial)

print("\nCase Insensitive Search")
case = [p for p in products if re.search(keyword, p, re.I)]
print(case)

print("\nReport")
print("Exact:", len(exact))
print("Prefix:", len(prefix))
print("Suffix:", len(suffix))
print("Partial:", len(partial))