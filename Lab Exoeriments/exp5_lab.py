from nltk.stem import PorterStemmer

# Create Porter Stemmer object
ps = PorterStemmer()

# List of words
words = ["playing", "studies", "running", "happiness", "jumped"]

print("Original Word\tStemmed Word")
print("-" * 30)

for word in words:
    print(word, "\t\t", ps.stem(word))