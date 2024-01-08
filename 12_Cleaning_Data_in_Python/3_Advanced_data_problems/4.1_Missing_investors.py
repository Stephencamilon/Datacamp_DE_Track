'''
Instructions:

1. Print the number of missing values by column in the banking DataFrame.
2. Plot and show the missingness matrix of banking with the msno.matrix() function.

'''

# Print number of missing values in banking
print(banking['inv_amount'].isna().sum())

# Visualize missingness matrix
msno.matrix(banking)
plt.show()
