import json
import os

# Load quotes from JSON
with open(os.path.join("utils", "calming_quotes.json"), "r") as f:
    quotes = json.load(f)

def get_quote(mood):
    """
    Returns a calming quote based on detected emotion.
    """
    return quotes.get(mood.lower(), ["You are enough."])[0]
