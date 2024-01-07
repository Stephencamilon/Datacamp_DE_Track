"""
Instructions:
1. Print the information of ride_sharing.
2. Use .describe() to print the summary statistics of the user_type column from ride_sharing.
"""

# Print the information of ride_sharing
print(ride_sharing.info())

# Print summary statistics of user_type column
print(ride_sharing['user_type'].describe())
