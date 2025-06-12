import json

with open("utils/calming_quotes.json", "r") as f:
    quotes = json.load(f)

def get_quote(mood):
    return quotes.get(mood.lower(), ["You are enough."])[0]
