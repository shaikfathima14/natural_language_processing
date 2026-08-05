import nltk
from nltk.tokenize import word_tokenize

# Download once
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

text = input("Enter a sentence: ")

words = word_tokenize(text)

tags = nltk.pos_tag(words)

print("POS Tags:")
print(tags)