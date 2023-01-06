import re

def check_password_strength(password):
    # Check the length of the password
    if len(password) < 8:
        return "Weak: Password is too short"
    # Check for the presence of uppercase and lowercase letters, digits, and special characters
    if not re.search(r'[A-Z]', password) or not re.search(r'[a-z]', password) or not re.search(r'[0-9]', password) or not re.search(r'[^A-Za-z0-9]', password):
        return "Weak: Password is missing required character types"
    # Check if the password is a common one
    with open('common_passwords.txt', 'r') as f:
        common_passwords = [line.strip() for line in f]
        if password in common_passwords:
            return "Weak: Password is a common one"
    # If the password passed all checks, it is considered strong
    return "Strong"

# Test the function with some example passwords
print(check_password_strength('abcdefgh'))
print(check_password_strength('abcdefGH'))
print(check_password_strength('abcdefGH1'))
print(check_password_strength('abcdefGH1!'))
print(check_password_strength('12345678'))
print(check_password_strength('password'))
print(check_password_strength('P@ssw0rd'))
