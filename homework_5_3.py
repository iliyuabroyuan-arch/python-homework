import string

text = input()

for symbol in string.punctuation:
    text = text.replace(symbol, "")

hashtag = "#" + "".join(word.capitalize() for word in text.split())
print(hashtag[:140])
