words = ["analyzing", "analysis", "analytical"]

print("{:<15} {:<15} {:<15} {:<18} {:<15}".format(
    "Original",
    "Root",
    "Affix",
    "Transformation",
    "Normalized"
))

for word in words:

    if word.endswith("ing"):
        suffix = "-ing"
        root = word[:-3]
        if root.endswith("z"):
            root += "e"
        transformation = "Inflectional"
        normalized = root

    elif word.endswith("sis"):
        suffix = "-sis"
        root = "analyze"
        transformation = "Derivational"
        normalized = root

    elif word.endswith("ical"):
        suffix = "-ical"
        root = "analyze"
        transformation = "Derivational"
        normalized = root

    else:
        suffix = "-"
        root = word
        transformation = "Unknown"
        normalized = word

    print("{:<15} {:<15} {:<15} {:<18} {:<15}".format(
        word,
        root,
        suffix,
        transformation,
        normalized
    ))

print("\nNormalized Representation:")

normalized_words = {}

for word in words:

    if word.endswith("ing"):
        root = word[:-3]
        if root.endswith("z"):
            root += "e"

    elif word.endswith("sis") or word.endswith("ical"):
        root = "analyze"

    else:
        root = word

    normalized_words.setdefault(root, []).append(word)

for root, variants in normalized_words.items():
    print(root, "-->", variants)