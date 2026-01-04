# test
import difflib

a = "thallium"
b = "thalium"

print(difflib.SequenceMatcher(None, a, b).ratio())