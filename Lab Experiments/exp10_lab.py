sentence = input("Enter a sentence: ")

words = sentence.split()

for word in words:
    tag = "NN"      # Initial tag

    if word.endswith("ing"):
        tag = "VBG"
    elif word.endswith("ed"):
        tag = "VBD"
    elif word[0].isupper():
        tag = "NNP"

    print(word, "->", tag)