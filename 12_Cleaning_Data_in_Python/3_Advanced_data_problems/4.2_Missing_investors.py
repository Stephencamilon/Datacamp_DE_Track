'''
Instructions:

Isolate the values of banking missing values of inv_amount into missing_investors and with non-missing inv_amount values into investors.

'''

# Print number of missing values in banking
print(banking.isna().sum())

# Visualize missingness matrix
msno.matrix(banking)
plt.show()

# Isolate missing and non missing values of inv_amount
missing_investors = banking[banking['inv_amount'].isna()]
investors = banking[~banking['inv_amount'].isna()]
