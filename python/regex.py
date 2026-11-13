# A Regular Expression is used to search, match, and manipulate text
# re functions are search, findall, split, sub etc.

import re

xyz = "Python"
match = re.search("Python", xyz) # Searches for a pattern in a string. Returns first match
if match:
    print("Text found")

abc = "cat bat mat"
result = re.findall("at", abc) # findall matches and returns a list.
print(result) # If no matches are found, an empty list is returned

text = "I love Java"
new_text = re.sub("Java", "Python", text) # sub replaces matched text.
print(new_text)

# The split() function returns a list where the string has been split at each match
rty = "Python is easy to learn"
x = re.split("\s", rty) # \s returns a match where the string contains a white space character
print(x)