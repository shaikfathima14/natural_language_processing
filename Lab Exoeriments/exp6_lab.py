# Bigram Model for Text Generation

text = input("Enter a sentence: ")

words = text.split()

print("Generated Bigrams:")

for i in range(len(words) - 1):
    print((words[i], words[i + 1]))