'''
Instructions:
1. Using the airlines DataFrame, store the length of each instance in the survey_response column in resp_length by using .str.len().
2. Isolate the rows of airlines with resp_length higher than 40.
3. Assert that the smallest survey_response length in airlines_survey is now bigger than 40.

'''

# Store length of each row in survey_response column
resp_length = airlines['survey_response'].str.len()

# Find rows in airlines where resp_length > 40
airlines_survey = airlines[resp_length > 40]

# Assert minimum survey_response length is > 40
assert airlines_survey['survey_response'].str.len().min() > 40

# Print new survey_response column
print(airlines_survey['survey_response'])
