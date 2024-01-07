'''
Instructions:

1. Change the capitalization of all values of dest_region to lowercase.
2. Replace the 'eur' with 'europe' in dest_region using the .replace() method.

'''

# Print unique values of both columns
print(airlines['dest_region'].unique())
print(airlines['dest_size'].unique())

# Lower dest_region column and then replace "eur" with "europe"
airlines['dest_region'] = airlines['dest_region'].str.lower()
airlines['dest_region'] = airlines['dest_region'].replace({'eur':'europe'})
