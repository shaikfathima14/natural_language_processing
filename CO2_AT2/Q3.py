from tabulate import tabulate

words = ["analyzing", "analysis", "analytical"]

results = []

for word in words:

    if word == "analyzing":
        root = "analyze"
        affix = "-ing"
        transformation = "Inflectional"
        normalized = "analyze"

    elif word == "analysis":
        root = "analyze"
        affix = "-sis"
        transformation = "Derivational"
        normalized = "analyze"

    elif word == "analytical":
        root = "analyze"
        affix = "-ical"
        transformation = "Derivational"
        normalized = "analyze"

    results.append([word, root, affix, transformation, normalized])

print(tabulate(results,
               headers=["Original Word",
                        "Root",
                        "Affix",
                        "Transformation",
                        "Normalized"],
               tablefmt="grid"))