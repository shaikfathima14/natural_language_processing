from nltk.stem import PorterStemmer

# Create Porter Stemmer object
ps = PorterStemmer()

# Get input from user
word = input("Enter a word: ")

# Perform stemming
stemmed_word = ps.stem(word)

# Display result
print("Original Word :", word)
print("Stemmed Word  :", stemmed_word)