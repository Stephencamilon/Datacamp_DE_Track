"""
Instructins:

1. Convert ride_date to a datetime object using to_datetime(), then convert the datetime object into a date and store it in ride_dt column.
2. Create the variable today, which stores today's date by using the dt.date.today() function.
3. For all instances of ride_dt in the future, set them to today's date.
4. Print the maximum date in the ride_dt column.
"""

# Convert tire_sizes to integer
ride_sharing['tire_sizes'] = ride_sharing['tire_sizes'].astype('int')

# Set all values above 27 to 27
ride_sharing.loc[ride_sharing['tire_sizes'] > 27, 'tire_sizes'] = 27

# Reconvert tire_sizes back to categorical
ride_sharing['tire_sizes'] = ride_sharing['tire_sizes'].astype('category')

# Print tire size description
print(ride_sharing['tire_sizes'].describe())
