import re

states = "Mississippi Alabama Texas Massachusetts Kansas"
# a) search for a word in variable states that ends in xas
# Store this word in element 0 of a list named statesList.
statesList = []
match = re.search(r'\b\w*xas\b', states)
if match:
    statesList.append(match.group())
# b) search for a word in states that begins with k and ends in s
# Perform a case-insensitive comparison. Store this word in element 1 of statesList.
match = re.search(r'\b\w*k\w*s\b', states, re.I)
if match:
    statesList.append(match.group())
# c) search for a word in states that begins with M and ends in s.
# Store this word in element 2 of the list.
match = re.search(r'\b\w*M\w*s\b', states)
if match:
    statesList.append(match.group())
# d) search for a word in states that ends in a.
# Store this word in element 3 of the list.
match = re.search(r'\b\w*a\b', states)
if match:
    statesList.append(match.group())
# e) search for a word that begins with M in states at the beginning of the string.
# Store this word at element 4 of the list.
match = re.search(r'^M\w+', states)
if match:
    statesList.append(match.group())
# f) Output the array states List to the screen
print(statesList)