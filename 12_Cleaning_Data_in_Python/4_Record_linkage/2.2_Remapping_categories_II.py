'''
Instructions:

As a first step, create a list of all possible matches, comparing 'italian' with the restaurant types listed in the cuisine_type column.

'''

# Create a list of matches, comparing 'italian' with the cuisine_type column
matches = process.extract('italian',  restaurants['cuisine_type'], limit = len(restaurants['cuisine_type']))

# Inspect the first 5 matches
print(matches[0:5])
