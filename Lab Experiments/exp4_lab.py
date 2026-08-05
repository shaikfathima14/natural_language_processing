# Function to generate plural forms

def pluralize(noun):
    if noun.endswith(("s", "x", "z", "ch", "sh")):
        return noun + "es"
    elif noun.endswith("y") and len(noun) > 1 and noun[-2].lower() not in "aeiou":
        return noun[:-1] + "ies"
    else:
        return noun + "s"


# Main Program
word = input("Enter a singular noun: ")

plural = pluralize(word)

print("Singular Noun :", word)
print("Plural Noun   :", plural)