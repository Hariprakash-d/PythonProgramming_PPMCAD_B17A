"""
---------------------------------------------------------------
Author: Hari Prakash D (ID: 14313, Batch-17A)
Date: 13-APR-2026
---------------------------------------------------------------

Login Authentication System:

Write a Python program that validates a user's login credentials based on specific security requirements.
The program should:
    1. Prompt the user to enter a username and password.
    2. Validate the username and password based on the following criteria:
        - The username must be at least 5 characters long and contain only alphanumeric characters.
        - The password must be at least 8 characters long, contain at least one digit.
    3. If the credentials are valid, print a success message. Otherwise, print an error message indicating which criteria were not met.
    
"""

def validate_username(username):
    if len(username) < 5:
        print("Username must be at least 5 characters long.")
        return False
    # if not username.isalnum():
    #     print("Username must contain only alphanumeric characters.")
    #     return False
    return True

def validate_password(password):
    if len(password) < 8:
        print("Password must be at least 8 characters long.")
        return False
    if not any(c.isdigit() for c in password):
        print("Password must contain at least one digit.")
        return False
    return True

# Get user input for username and password
username = input("Enter your username: ")   
password = input("Enter your password: ")
# Validate username and password
username_error = validate_username(username)
password_error = validate_password(password)
if not username_error:
    print("Username Error:", username_error)
if not password_error:
    print("Password Error:", password_error)
if username_error and password_error:
    print("Login successful!")
    print("Return: True")

