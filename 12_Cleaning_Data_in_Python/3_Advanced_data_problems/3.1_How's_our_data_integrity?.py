'''
Instructions:

1. Find the rows where the sum of all rows of the fund_columns in banking are equal to the inv_amount column.
2. Store the values of banking with consistent inv_amount in consistent_inv, and those with inconsistent ones in inconsistent_inv.

'''

# Store fund columns to sum against
fund_columns = ['fund_A', 'fund_B', 'fund_C', 'fund_D']

# Find rows where fund_columns row sum == inv_amount
inv_equ = banking[fund_columns].sum(axis=1) == banking['inv_amount']

# Store consistent and inconsistent data
consistent_inv = banking[inv_equ]
inconsistent_inv = banking[~inv_equ]

# Store consistent and inconsistent data
print("Number of inconsistent investments: ", inconsistent_inv.shape[0])
