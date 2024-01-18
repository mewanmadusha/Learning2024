# Create a function is_valid_email that takes an email address as input and returns True 
# if the email address is valid, and False otherwise. The email address should follow the 
# standard format,including a local part, the '@' symbol, and a domain part. 
# For example: user@example.com.

import re

def check_valid_email(email):
    # Define a regular expression pattern for a basic email format
    # ^ consider as the begining
    # [a-zA-Z0-9_.+-] any text with given special characters
    # @[a-zA-Z0-9-] check @ and after any text in the string
    #\.[a-zA-Z0-9-.] check "."included and any text in the string can have another "." as well
    #  $ consider this as the end

    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    
    # Use re.match to check if the email matches the pattern
    match = re.match(pattern, email)
    
    # If there's a match, the email is valid
    return match is not None

emailex = "user@example.com"
email1 = "mewan@example.com"
email2 = "madusha@com"
email3 = "another_user@domain.co.jp"

print(f"Is '{email1}' a valid email? {check_valid_email(email1)}")
print(f"Is '{email1}' a valid email? {check_valid_email(email1)}")
print(f"Is '{email2}' a valid email? {check_valid_email(email2)}")
print(f"Is '{email3}' a valid email? {check_valid_email(email3)}")