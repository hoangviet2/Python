import json
from difflib import get_close_matches
data = json.load(open("data.json"))
def translate(word):
    if word.lower() in data:
        return data[word.lower()]
    elif len(get_close_matches(word,data.keys()))>0:
        return "Did you mean %s instead" %get_close_matches(word,data.keys())[0]
    else:
        return "word doesn't exists. Please double check it"
word = input("Enter word: ")
print(translate(word))