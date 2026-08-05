# Simple probabilistic POS tagging

pos_dict = {
    "I": "PRON",
    "eat": "VERB",
    "rice": "NOUN",
    "she": "PRON",
    "plays": "VERB",
    "cricket": "NOUN"
}

sentence = input("Enter a sentence: ")

words = sentence.split()

for word in words:
    print(word, "->", pos_dict.get(word, "UNKNOWN"))