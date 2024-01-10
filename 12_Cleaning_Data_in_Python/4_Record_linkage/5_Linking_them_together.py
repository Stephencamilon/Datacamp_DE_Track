'''
Instructions:

1. Isolate instances of potential_matches where the row sum is above or equal to 3 by using the .sum() method.
2. Extract the second column index from matches, which represents row indices of matching record from restaurants_new by using the .get_level_values() method.
3. Subset restaurants_new for rows that are not in matching_indices.
4. Append non_dup to restaurants.


'''

# Isolate potential matches with row sum >=3
matches = potential_matches[potential_matches.sum(axis=1) >= 3]

# Get values of second column index of matches
matching_indices = matches.index.get_level_values(1)

# Subset restaurants_new based on non-duplicate values
non_dup = restaurants_new[~restaurants_new.index.isin(matching_indices)]

# Append non_dup to restaurants
full_restaurants = restaurants.append(non_dup)
print(full_restaurants)
