# Print the header of account_opened
print(banking['account_opened'].head())

# Convert account_opened to datetime
banking['account_opened'] = pd.to_datetime(banking['account_opened'],
                                           # Infer datetime format
                                           infer_datetime_format = True,
                                           # Return missing value for error
                                           errors = 'coerce') 


# infer_datetime_format=True, tries to match the inputted datetime strings from sets of known datetime formats.
# errors = 'coerce', outputs NaT (Not a Time) value when there are errors during the conversation of inferrence of the previous argument.
