'''
Instructions:

1. Print the categories DataFrame and take a close look at all possible correct categories of the survey columns.
2. Print the unique values of the survey columns in airlines using the .unique() method.
'''

# Print categories DataFrame
print(categories)

# Print unique values of survey columns in airlines
print('Cleanliness: ', airlines['cleanliness'].unique(), "\n")
print('Safety: ', airlines['safety'].unique(), "\n")
print('Satisfaction: ', airlines['satisfaction'].unique(), "\n")
