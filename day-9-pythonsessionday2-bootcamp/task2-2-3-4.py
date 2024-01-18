
# Domain Extraction:
# Create a function extract_domain that takes an email address 
# as input and returns the domain part (after the '@' symbol). 
# For example, if the email is user@example.com, the function should return example.com.

import re

def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    match = re.match(pattern, email)
    return match is not None

def extract_domain(email):
    if not is_valid_email(email):
        return "not a valid email"
    
    # Split the email address using '@' as the delimiter
    parts = email.split('@')
    
    # Return the second part, which is the domain
    return parts[1]

def extract_username(email):
    if not is_valid_email(email):
        return "not a valid email"
    parts = email.split('@')
    
    # Return the first part(username)
    return parts[0]

email1 = "user@example.com"
email2 = "invalid_email@com"
email3 = "another_user@domain.co.uk"

# print(f"Domain of '{email1}': {extract_domain(email1)}")
# print(f"Domain of '{email2}': {extract_domain(email2)}")
# print(f"Domain of '{email3}': {extract_domain(email3)}")


print(f"username of '{email1}': {extract_username(email1)}")
print(f"username of '{email2}': {extract_username(email2)}")
print(f"username of '{email3}': {extract_username(email3)}")

