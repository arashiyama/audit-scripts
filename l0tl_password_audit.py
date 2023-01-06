'''
This script works by using the "net user" command to get a list of users and their encrypted passwords. 
It then prompts the user to enter the password for each user, and checks the strength of the password using the same checks as in the previous version of the script. 
Note that this script requires the user to manually enter the password for each user, which may not be practical in a large network. 
It is also possible that the user may not have permission to view the encrypted passwords, in which case the script will not be able to function. 
'''
import subprocess
import re

def get_users_and_hashes():
    # Use the net user command to get a list of users and their encrypted passwords
    users_and_hashes = subprocess.check_output(["net", "user"])
    # Split the output into a list of lines
    lines = [line.strip() for line in users_and_hashes.split("\n")]
    # Extract the username and encrypted password for each line
    users_and_hashes = []
    for line in lines:
        if ":" in line:
            username, _, hash = line.partition(":")
            users_and_hashes.append((username, hash))
    return users_and_hashes

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

Get a list of users and their encrypted passwords
users_and_hashes = get_users_and_hashes()

Check the strength of the password for each user
for username, hash in users_and_hashes:
password = input("Enter the password for {}: ".format(username))
strength = check_password_strength(password)
print("{}'s password is {}".format(username, strength))