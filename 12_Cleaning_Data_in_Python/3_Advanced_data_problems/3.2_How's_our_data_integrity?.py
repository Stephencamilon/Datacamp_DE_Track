'''
Instructions:

1. Store today's date into today, and manually calculate customers' ages and store them in ages_manual.
2. Find all rows of banking where the age column is equal to ages_manual and then filter banking into consistent_ages and inconsistent_ages

'''

# Store today's date and find ages
today = dt.date.today()
ages_manual = today.year - banking['birth_date'].dt.year

# Find rows where age column == ages_manual
age_equ = banking['age'] == ages_manual

# Store consistent and inconsistent data
consistent_ages = banking[age_equ]
inconsistent_ages = banking[~age_equ]

# Store consistent and inconsistent data
print("Number of inconsistent ages: ", inconsistent_ages.shape[0])
