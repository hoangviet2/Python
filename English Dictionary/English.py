import json
from difflib import get_close_matches
from os import pipe
data = json.load(open("data.json"))
def translate(word):
    if word.lower() in data:
        return data[word.lower()]
    elif word.title() in data: #if user entered "texas" this will check for "Texas" as well.
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word,data.keys()))>0:
        yn = input("Did you mean %s instead? Enter Y for Yes and N for No " %get_close_matches(word,data.keys())[0])
        if yn == 'Y':
            return data[get_close_matches(word,data.keys())[0]]
        elif yn == 'N':
            return "word doesn't exists. Please double check it"
        else:
            return "we didn't understand you"
    else:
        return "word doesn't exists. Please double check it"
word = input("Enter word: ")
output = translate(word)
if type(output) == list:
    for items in output:
        print(items)
else:
    print(output)