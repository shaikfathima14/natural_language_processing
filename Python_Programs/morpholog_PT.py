# Morphology and Word Formation Implementation

word = input("Enter a word: ")

prefixes = ["un", "re", "dis", "pre"]
suffixes = ["ing", "ed", "ness", "ly", "er"]

prefix = ""
suffix = ""
root = word

# Check Prefix
for p in prefixes:
    if word.startswith(p):
        prefix = p
        root = word[len(p):]
        break

# Check Suffix
for s in suffixes:
    if root.endswith(s):
        suffix = s
        root = root[:-len(s)]
        break

print("\nMorphological Analysis")
if prefix:
    print("Prefix :", prefix)
print("Root Word :", root)
if suffix:
    print("Suffix :", suffix)