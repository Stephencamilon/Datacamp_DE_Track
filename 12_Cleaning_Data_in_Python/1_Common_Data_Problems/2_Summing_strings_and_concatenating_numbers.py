"""
Instructions:

1. Use the .strip() method to strip duration of "minutes" and store it in the duration_trim column.
2. Convert duration_trim to int and store it in the duration_time column.
3. Write an assert statement that checks if duration_time's data type is now an int.
4. Print the average ride duration.

"""


# Strip duration of minutes
ride_sharing['duration_trim'] = ride_sharing['duration'].str.strip('minutes')

# Convert duration to integer
ride_sharing['duration_time'] = ride_sharing['duration_trim'].astype('int')

# Write an assert statement making sure of conversion
assert ride_sharing['duration_time'].dtype == 'int'

# Print formed columns and calculate average ride duration 
print(ride_sharing[['duration','duration_trim','duration_time']])
print(ride_sharing['duration_time'].mean())
